import datetime as dt

class Milion_days_Iterator:

    def __init__(self, date, max):
        self.date = date
        self.maxdays = max

    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.maxdays -= 1
        self.date += dt.timedelta(days=1)
        return ret

class Milion_days:

    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays
        self.iterator = Milion_days_Iterator(self.date, self.maxdays)

    def __iter__(self):
        return self.iterator

md = Milion_days(2000, 1, 1, 3)
print(next(iter(md)))
for d in md:
    print(d)
