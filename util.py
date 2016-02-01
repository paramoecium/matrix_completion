from datetime import datetime
class Timer(object):
    def __init__(self, name=None, verbose=2):
        self.name = name
        self.verbose = verbose;

    def __enter__(self):
        if self.name and self.verbose >= 1:
            print '...', self.name
            self.start = datetime.now()
            return self

    def __exit__(self, type, value, traceback):
        if self.verbose >= 2:                           
            if self.name:
                print '...', self.name, "done in", datetime.now() - self.start
            else:
                print '... done in', datetime.now() - self.start

    def now_time(self):
        return datetime.now() - self.start
