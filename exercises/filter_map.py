from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        """
        Реализовать функцию, которая ведет себя как filter и map. К каждому значению из
        списка применяется функция, которая в ответ возвращает кортеж
        (булево значение, результат работы функции,).
        Если первый элемент кортежа истина, то результат добавляется в список.

        Принимает в качестве аргументов функцию и итерируемый источник, а возвращает список.
        :param func: Функция, применяемая к каждому элементу списка.
        :param input_array: Исходный список.
        :return: Отфильтрованный список.
        """

        def inner_filter_map(iter_list, res_list):
            if iter_list == []:
                return res_list

            head, *tail = iter_list
            new_elem = func(head)
            if new_elem[0]:
                res_list.append(new_elem[1])
            return inner_filter_map(tail, res_list)

        result_list = []
        return inner_filter_map(input_array, result_list)
