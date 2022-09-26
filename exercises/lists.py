from functools import reduce


class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        maximum: int = reduce(lambda acc, el: el if acc <= el else acc, input_list, 0)
        return list(map(lambda el: maximum if el > 0 else el, input_list))

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        low: int = 0
        high: int = len(input_list) - 1
        return ListExercise.bin_search(input_list, query, low, high)

    @staticmethod
    def bin_search(input_list: list[int], query: int, low: int, high: int) -> int:
        if low > high:
            return -1

        mid: int = (low + high) // 2
        if query == input_list[mid]:
            return mid
        elif query < input_list[mid]:
            return ListExercise.bin_search(input_list, query, low, mid - 1)
        else:
            return ListExercise.bin_search(input_list, query, mid + 1, high)
