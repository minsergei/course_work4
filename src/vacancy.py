import json
# from src.saverjs import JsonSaver
# import os


class Vacancy:
    vacancy_list = []

    def __init__(self, name, experience, salary_from, salary_to, snippet, url):
        self.name = name
        self.experience = experience
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.snippet = snippet
        self.url = url

    def __repr__(self):
        """
        :return: Возвращает словарь для инициализации объекта
        """
        dict_vacancy = (f'"name": "{self.name}", "experience": "{self.experience}", "salary_from": {self.salary_from}, '
                        f'"salary_to": {self.salary_to}, "snippet": "{self.snippet}", "url": "{self.url}"')
        return '{' + dict_vacancy + '}'

    def __str__(self):
        """
        Описание объекта вакансии
        """
        return (f"\nВакансия: {self.name}\nЗарплата: {self.salary_from} руб. - {self.salary_to} руб.\n"
                f"Опыт работы: {self.experience}\nОписание: {self.snippet}")

    def __lt__(self, other):
        """
        Магические методы для сравнение и сортировки объктов по зарплате
        """
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from < other.salary_from
            else:
                return self.salary_from < other.salary_to
        elif other.salary_from > 0:
            return self.salary_to < other.salary_from
        else:
            return self.salary_to < other.salary_to

    def __le__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from <= other.salary_from
            else:
                return self.salary_from <= other.salary_to
        elif other.salary_from > 0:
            return self.salary_to <= other.salary_from
        else:
            return self.salary_to <= other.salary_to

    def __gt__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from > other.salary_from
            else:
                return self.salary_from > other.salary_to
        elif other.salary_from > 0:
            return self.salary_to > other.salary_from
        else:
            return self.salary_to > other.salary_to

    def __ge__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from >= other.salary_from
            else:
                return self.salary_from >= other.salary_to
        elif other.salary_from > 0:
            return self.salary_to >= other.salary_from
        else:
            return self.salary_to >= other.salary_to

    def __eq__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from == other.salary_from
            else:
                return self.salary_from == other.salary_to
        elif other.salary_from > 0:
            return self.salary_to == other.salary_from
        else:
            return self.salary_to == other.salary_to

    def __ne__(self, other):
        if self.salary_from > 0:
            if other.salary_from > 0:
                return self.salary_from != other.salary_from
            else:
                return self.salary_from != other.salary_to
        elif other.salary_from > 0:
            return self.salary_to != other.salary_from
        else:
            return self.salary_to != other.salary_to

    @classmethod
    def cast_to_object_list(cls, vacancy_json):
        """
        Класс-метод для создания экземпляров вакансий из файла json и добавления в общий список
        :param vacancy_json:
        :return:
        """
        for item in vacancy_json:
            vacancy = cls(item["name"], item["experience"], item["salary_from"], item["salary_to"],
                          item["snippet"], item["url"])
            Vacancy.vacancy_list.append(vacancy)

    @staticmethod
    def get_top(top: int):
        """
        Выводит топ вакансий по зарплате
        """
        sorted_vacancy = sorted(Vacancy.vacancy_list, reverse=True)
        top = (sorted_vacancy[:top])
        [print(i) for i in top]
        return json.loads(repr(top))