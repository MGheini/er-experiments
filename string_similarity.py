import rltk


def match_records_using_string_similarity(record_1, field_1, record_2, field_2):
    value_1 = getattr(record_1, field_1).lower()
    value_2 = getattr(record_2, field_2).lower()

    ngram_tokenizer = rltk.NGramTokenizer()
    if rltk.jaccard_index_similarity(ngram_tokenizer.basic(value_1, 3),
                                     ngram_tokenizer.basic(value_2, 3)) > 0.8:
        return True
    return False
