from contextlib import contextmanager


class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query2(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')