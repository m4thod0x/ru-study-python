from typing import Union
from functools import reduce


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk), у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def check_condition(film: dict) -> bool:
            check_raiting = film["rating_kinopoisk"] != "" and float(film["rating_kinopoisk"]) > 0
            check_country = film["country"] != "" and len(film["country"].split(",")) >= 2
            return check_raiting and check_country

        checked_list = [film for film in list_of_movies if check_condition(film)]
        mapped_list = list(map(lambda film: float(film["rating_kinopoisk"]), checked_list))
        result = reduce(lambda acc, rating: acc + rating, mapped_list, 0) / len(mapped_list)
        return result

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def filter_movie(movie: dict) -> bool:
            if movie["rating_kinopoisk"] == "":
                return False
            elif float(movie["rating_kinopoisk"]) < rating:
                return False
            else:
                return True

        filtered_movies = [movie for movie in list_of_movies if filter_movie(movie)]
        list_of_names = list(map(lambda movie: movie["name"], filtered_movies))
        result = reduce(lambda acc, name: acc + name.count("и"), list_of_names, 0)
        return result
