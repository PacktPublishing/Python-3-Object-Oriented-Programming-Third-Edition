from functools import total_ordering


@total_ordering
class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return f"{self.string}:{self.number}"

    def __eq__(self, object):
        return all(
            (
                self.string == object.string,
                self.number == object.number,
                self.sort_num == object.number,
            )
        )

