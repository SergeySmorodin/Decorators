from task_2 import logger
import re

path = 'log_4.log'

lst = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


class FlatIterator:
    @logger(path)
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cursor = 0
        self.inner_cursor = 0

    @logger(path)
    def __iter__(self):
        return self

    @logger(path)
    def __next__(self):
        while self.cursor < len(self.list_of_list):
            if self.inner_cursor < len(self.list_of_list[self.cursor]):
                result = self.list_of_list[self.cursor][self.inner_cursor]
                self.inner_cursor += 1
                return result
            else:
                self.cursor += 1
                self.inner_cursor = 0
        raise StopIteration


for i in FlatIterator(lst):
    print(i)


@logger(path)
def format_phone(phone):
    pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})(\s*\(?(доб\.)?\s*(\d+)\)?)?'
    )
    substitution = r'+7(\2)\3-\4-\5 \7\8'
    return pattern.sub(substitution, phone).strip()


result = format_phone('8 495947 88 09')
