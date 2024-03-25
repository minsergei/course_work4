from src.parser_hh import Parser, HeadHunterAPI
from src.vacancy import Vacancy
from src.saverjs import JsonSaver
from src.func import get_filter_vacancies, get_ranged_vacancies
import os


def user_interaction():
    hh = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    pars_hh = Parser(hh.load_vacancies(search_query))
    list_vacancies = pars_hh.get_pars()

    path_json = os.path.abspath('data/vacancies.json')
    json_saver = JsonSaver(path_json, "r+")
    json_saver.add_vacancy(list_vacancies)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = get_filter_vacancies(json_saver.read_file(), filter_words)

    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    ranged_vacancies = get_ranged_vacancies(filtered_vacancies, salary_range)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    Vacancy.cast_to_object_list(ranged_vacancies)
    top_vacancies = Vacancy.get_top(top_n)

    path_json_top = os.path.abspath('data/top.json')
    json_saver_top = JsonSaver(path_json_top, "w")
    json_saver_top.add_vacancy(top_vacancies)


if __name__ == "__main__":
    user_interaction()
