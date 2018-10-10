import rltk

from records import *
from random import shuffle
from collections import defaultdict
from string_similarity import match_records_using_string_similarity


def get_datasets_from_csvs(csv_path_1, record_1, csv_path_2, record_2):
    dataset_1 = rltk.Dataset(reader=rltk.CSVReader(csv_path_1), record_class=record_1, adapter=rltk.MemoryAdapter())
    dataset_2 = rltk.Dataset(reader=rltk.CSVReader(csv_path_2), record_class=record_2, adapter=rltk.MemoryAdapter())

    return dataset_1, dataset_2


def get_ground_truth(gt_csv_path, field_1, field_2):
    gt = rltk.GroundTruth(field_1, field_2)
    gt.load(gt_csv_path)

    return gt


def get_train_test_splits(dataset_1, dataset_2, gt: rltk.GroundTruth, train_test_ratio=9):
    pairs = rltk.get_record_pairs(dataset_1, dataset_2)

    positive_pairs = []
    negative_pairs = []

    for r1, r2 in pairs:
        if gt.is_member(r1.id, r2.id):
            positive_pairs.append((r1, r2))
        else:
            negative_pairs.append((r1, r2))

    train_pairs = []
    test_pairs = []

    # stratified split
    for i, p in enumerate(positive_pairs):
        if i % (train_test_ratio + 1) == 0:
            test_pairs.append((p, 1))
        else:
            train_pairs.append((p, 1))
    for i, p in enumerate(negative_pairs):
        if i % (train_test_ratio + 1) == 0:
            test_pairs.append((p, 0))
        else:
            train_pairs.append((p, 0))

    shuffle(train_pairs)
    shuffle(test_pairs)

    return train_pairs, test_pairs


def get_inverted_indexes_based_on_field(dataset_1, field_1, dataset_2, field_2):
    index = {'dataset_1': defaultdict(list), 'dataset_2': defaultdict(list)}

    for r in dataset_1:
        index['dataset_1'][getattr(r, field_1)].append(r)
    for r in dataset_2:
        index['dataset_2'][getattr(r, field_2)].append(r)

    return index


def get_train_test_splits_using_index(index, gt: rltk.GroundTruth, train_test_ratio=9):
    positive_pairs = []
    negative_pairs = []

    for k in index['dataset_1']:
        for r1 in index['dataset_1'][k]:
            for r2 in index['dataset_2'][k]:
                if gt.is_member(r1.id, r2.id):
                    positive_pairs.append((r1, r2))
                else:
                    negative_pairs.append((r1, r2))

    train_pairs = []
    test_pairs = []

    # stratified split
    for i, p in enumerate(positive_pairs):
        if i % (train_test_ratio + 1) == 0:
            test_pairs.append((p, 1))
        else:
            train_pairs.append((p, 1))
    for i, p in enumerate(negative_pairs):
        if i % (train_test_ratio + 1) == 0:
            test_pairs.append((p, 0))
        else:
            train_pairs.append((p, 0))

    shuffle(train_pairs)
    shuffle(test_pairs)

    return train_pairs, test_pairs


def evaluate(test, pred_labels):
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for i, (pair, label) in enumerate(test):
        if label == 1 and label == pred_labels[i]:
            print('{} <--> {}'.format(pair[0].id, pair[1].id))
            tp += 1
        elif label == 0 and label != pred_labels[i]:
            fp += 1
        elif label == 0 and label == pred_labels[i]:
            tn += 1
        else:
            fn += 1

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = (2 * precision * recall) / (precision + recall)

    return precision, recall, f1


if __name__ == '__main__':
    dataset_1, dataset_2 = get_datasets_from_csvs('data/dblp-scholar/DBLP1.csv', DBLPRecord,
                                                  'data/dblp-scholar/Scholar.csv', ScholarRecord)
    gt = get_ground_truth('data/dblp-scholar/DBLP-Scholar_perfectMapping.csv', 'idDBLP', 'idScholar')
    # for large datasets
    index = get_inverted_indexes_based_on_field(dataset_1, 'year', dataset_2, 'year')
    train, test = get_train_test_splits_using_index(index, gt)
    print(len(train))
    print(len(test))

    pred_labels = []

    for pair, label in test:
        pred_labels.append(int(match_records_using_string_similarity(pair[0], 'title', pair[1], 'title')))

    precision, recall, f1 = evaluate(test, pred_labels)

    print('precision: {}, recall: {}, f1: {}'.format(precision, recall, f1))
