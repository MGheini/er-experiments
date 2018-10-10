import rltk


class AmazonRecord(rltk.Record):
    @property
    def id(self):
        return self.raw_object['id']

    @property
    def title(self):
        return self.raw_object['title']

    @property
    def description(self):
        return self.raw_object['description']

    @property
    def manufacturer(self):
        return self.raw_object['manufacturer']

    @property
    def price(self):
        return self.raw_object['price']


class GoogleRecord(rltk.Record):
    @property
    def id(self):
        return self.raw_object['id']

    @property
    def name(self):
        return self.raw_object['name']

    @property
    def description(self):
        return self.raw_object['description']

    @property
    def manufacturer(self):
        return self.raw_object['manufacturer']

    @property
    def price(self):
        return self.raw_object['price']


class AbtRecord(rltk.Record):
    @property
    def id(self):
        return self.raw_object['id']

    @property
    def name(self):
        return self.raw_object['name']

    @property
    def description(self):
        return self.raw_object['description']

    @property
    def price(self):
        return self.raw_object['price']


class BuyRecord(rltk.Record):
    @property
    def id(self):
        return self.raw_object['id']

    @property
    def name(self):
        return self.raw_object['name']

    @property
    def description(self):
        return self.raw_object['description']

    @property
    def price(self):
        return self.raw_object['price']

    @property
    def manufacturer(self):
        return self.raw_object['manufacturer']


class DBLPRecord(rltk.Record):
    @property
    def id(self):
        return self.raw_object['id']

    @property
    def title(self):
        return self.raw_object['title']

    @property
    def authors(self):
        return '' if self.raw_object['authors'] == 'N/A' else self.raw_object['authors']

    @property
    def venue(self):
        return '' if self.raw_object['venue'] == 'N/A' else self.raw_object['venue']

    @property
    def year(self):
        return self.raw_object['year']


class ScholarRecord(rltk.Record):
    @property
    def id(self):
        return self.raw_object['id']

    @property
    def title(self):
        return self.raw_object['title']

    @property
    def authors(self):
        return self.raw_object['authors']

    @property
    def venue(self):
        return self.raw_object['venue']

    @property
    def year(self):
        return self.raw_object['year']


class ACMRecord(rltk.Record):
    @property
    def id(self):
        return self.raw_object['id']

    @property
    def title(self):
        return self.raw_object['title']

    @property
    def authors(self):
        return self.raw_object['authors']

    @property
    def venue(self):
        return self.raw_object['venue']

    @property
    def year(self):
        return self.raw_object['year']
