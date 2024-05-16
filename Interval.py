class Interval:
    def __init__(self, min, max):
        self.__min = min
        self.__max = max

    @classmethod
    def createInterval(cls, min, max):
        if min == max:
            return None
        if min < max:
            return cls(min, max)
        return cls(max, min)

    @property
    def min(self):
        return self.__min

    @min.getter
    def min(self):
        return self.__min

    @min.setter
    def min(self, value):
        if value < self.__max:
            self.__min = value

    @min.deleter
    def min(self):
        del self.__min

    def _get_max(self):
        return self.__max

    def _set_max(self, value):
        if value > self.__min:
            self.__max = value

    def _del_max(self):
        del self.__max

    max = property(fget=_get_max, fset=_set_max, fdel=_del_max, doc="The max value of the interval")

    def __str__(self):
        return str("[" + str(self.__min) + ";" + str(self.__max) + "]")

    def __eq__(self, other):
        if self.__min == other.min and self.__max == other.max:
            return True
        else:
            return False

    def __add__(self, other):
        if self.is_intersection(other):
            return Interval.createInterval((other.max, self.__max)[(self.__max > other.max)],
                                           (other.min, self.__min)[(self.__min < other.min)])
        return None

    def intersection(self, other):
        if self == other:
            return self
        if self.is_intersection(other):
            return Interval.createInterval((self.__max, other.max)[(self.__max > other.max)],
                                           (self.__min, other.min)[(self.__min < other.min)])
        return None

    def is_intersection(self, other):
        if self.__min > other.max or self.__max < other.min:
            return False
        return True
