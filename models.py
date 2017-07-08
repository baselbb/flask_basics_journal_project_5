import datetime
from peewee import *


# all caps means we want this to be constant for developers
DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    """Entry model table in database and fields for a blog entry"""
    title = CharField(max_length=100)
    date = DateTimeField(default=datetime.datetime.now)
    spent = CharField(max_length=100)
    learned = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-date',)

    # class method to generate new journal entries
    @classmethod
    def create_entry(cls, title, date, spent, learned, resources):
        try:
            # we added the with with transaction - if this works go ahead, otherwise forget what you did
            with DATABASE.transaction():
                cls.create(
                    title=title,
                    date=date,
                    spent=spent,
                    learned=learned,
                    resoruces=resources)
        # if username or email are not unique it will throw the error
        # here we also raise a  value error to the user
        except IntegrityError:
            raise ValueError("Title. already exists.  Enter another title!")


def initialize():
    """initialize the database"""
    DATABASE.get_conn()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()
