class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list_index = 0
        self.item_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_index >= len(self.list_of_list):  # остановим итератор, если индекс выйдет из длины первичного списка
            raise StopIteration

        tmp = self.list_of_list[self.list_index]
        # проверка вхождения индекса
        if self.item_index >= len(tmp):  # если индекс >= длины вложенного списка
            self.list_index += 1  # меняем индекс на следующий список
            self.item_index = 0  # указываем на начало следующего вложенного списка
            return self.__next__()  # новая итерация

        # если выход и переход на следующую итерацию не совершены, заполняем список
        item = tmp[self.item_index]
        self.item_index += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
