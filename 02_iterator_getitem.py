import datetime as dt

class Milion_days:

    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays

    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration()

md = Milion_days(2000, 1, 1, 2)
#print(md[0], md[3], md[10])
it = iter(md)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
#for d in md:
    #print(d)
