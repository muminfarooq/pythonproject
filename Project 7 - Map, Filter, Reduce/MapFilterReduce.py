"""
Map, Filter, Reduce
Jimmy Tran
"""


class MfrList(list):
    """A class that's a Python list with map(), filter(), reduce() added"""

    @staticmethod
    def validate_func(func):
        """Validate func is callable, raises TypeError if not"""
        if not callable(func):
            raise TypeError(f"'{type(func)}' is not callable")

    def map(self, func):
        """Applies func to each element, returns a new MfrList"""
        self.validate_func(func)
        return MfrList([func(e) for e in self])

    def filter(self, func):
        """Applies func to each element, producing True or False for each, returns a new MfrList with True elements"""
        self.validate_func(func)
        return MfrList([e for e in self if func(e) is True])

    def reduce(self, func, initial=None):
        """Applies func to each element, returns a new MfrList"""
        if initial is None and not self:
            raise TypeError("The initial is None and the list is empty")
        elif initial is None and len(self) == 1:
            return self[0]
        elif initial is None and len(self) > 1:
            first = self[0]
            for i in self[1:]:
                first = func(first, i)
            return first
        elif initial is not None and not self:
            return initial
        elif initial is not None and len(self) > 0:
            first = initial
            for i in self[0:]:
                first = func(first, i)
            return first


# map() example
def square(mfrlist):
    """Square every element in the list"""
    return mfrlist.map(lambda x: x ** 2)


# filter() example
def odds(mfrlist):
    """Return a new list with all the odd numbers in the list"""
    return mfrlist.filter(lambda x: x % 2 == 1)


# reduce() example
def add_all(mfrlist):
    """Sum up all elements in the list"""
    return mfrlist.reduce(lambda a, b: a + b, 0)


# map()/reduce() example
def sum_of_squares(mfrlist):
    """Add up the squares of all elements in the list"""
    return (mfrlist
            .map(lambda x: x ** 2)
            .reduce(lambda a, b: a + b, 0))


def is_in(mfrlist, key):
    """Return True if key is in mfrlist, False otherwise"""
    return (mfrlist
            .map(lambda e: e == key)
            .reduce(lambda a, b: a or b, False))


def capitalize(mfrlist):
    return (mfrlist
            .map(lambda e: str.capitalize(e)))


def between(mfrlist, inclusive_start, exclusive_end):
    if mfrlist and not hasattr(mfrlist[0], "__lt__"):
        raise TypeError("mfrlist should consist of numbers only or strings only")
    return (mfrlist
            .filter(lambda x: inclusive_start <= x < exclusive_end))


def oldest(mfrlist):
    if not mfrlist:
        raise TypeError("mfrlist cannot be empty")
    return (mfrlist
            .reduce(lambda a, b: a if a[1] >= b[1] else b)[0])


def join(mfrlist, sep):
    if not mfrlist:
        return ""
    return str((mfrlist
                .reduce(lambda a, b: a if len(mfrlist) == 1 else str(a) + str(sep) + str(b))))


def same(mfrlist):
    if not mfrlist or len(mfrlist) == 1:
        return True
    else:
        return (mfrlist
                .map(lambda x: True if x == mfrlist[0] else False)
                .reduce(lambda a, b: True if a and b else False))


def abs_of_evens(mfrlist):
    return (mfrlist
            .filter(lambda x: x % 2 == 0)
            .map(lambda y: abs(y)))


def count_str(mfrlist, key):
    return (mfrlist
            .map(lambda x: 1 if str.upper(x) == str.upper(key) else 0)
            .reduce(lambda a, b: a + b))


def longest_palindrome(mfrlist):
    if not mfrlist:
        raise TypeError("mfrlist should not be empty")
    return (mfrlist
            .filter(lambda x: x == x[::-1])
            .reduce(lambda a, b: a if len(a) >= len(b) else b))


def test():
    """Sample usage"""
    mfrlist = MfrList([12, 98, 53])
    mfrlist2 = MfrList(["anakin", "skywalker", "dARTH", "vADER"])
    mfrlist_age = MfrList([("John", 28), ("Mary", 30), ("Jake", 5)])
    print(f"square({mfrlist}) => {square(mfrlist)}")
    print(f"add_all({mfrlist}) => {add_all(mfrlist)}")
    print(f"odds({mfrlist}) => {odds(mfrlist)}")
    print(f"is_in({mfrlist} => {is_in(mfrlist, 98)}")
    print(f"is_in({mfrlist2} => {capitalize(mfrlist2)}")
    print(f"join({mfrlist2} => {join(mfrlist2, '-')}")
    print(f"oldest({mfrlist_age} => {oldest(mfrlist_age)}")


if __name__ == '__main__':
    test()
