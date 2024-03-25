from src.parser_hh import Parser, HeadHunterAPI
from src.vacancy import Vacancy
from src.saverjs import JsonSaver
from src.func import get_filter_vacancies, get_ranged_vacancies
import os


def user_interaction():
    # Получаем вакансии с hh.ru. Изменяем данные под структуру json-файла и для создания объектов класса вакансии
    hh = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    pars_hh = Parser(hh.load_vacancies(search_query))
    list_vacancies = pars_hh.get_pars()
    # Сохраняем данные в json-файл с помощью метода класса JsonSaver
    path_json = os.path.abspath('data/vacancies.json')
    json_saver = JsonSaver(path_json, "w")
    json_saver.add_vacancy(list_vacancies)
    # Фильтруем данные по описанию вакансии
    filter_words = input("Введите ключевые слова для фильтрации вакансий(через пробел): ").split()
    filtered_vacancies = get_filter_vacancies(json_saver.read_file(), filter_words)
    # Фильтруем данные по диапозону цен
    salary_range = input("Введите диапазон зарплат(Пример: 100000 - 150000): ")
    ranged_vacancies = get_ranged_vacancies(filtered_vacancies, salary_range)
    # Создаем список с объектами класса вакансия, и методом получаем топ N отсортированных вакансий
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    Vacancy.cast_to_object_list(ranged_vacancies)
    top_vacancies = Vacancy.get_top(top_n)
    # Сохраняем данные по топ вакансиям в json-файл с помощью метода класса JsonSaver
    path_json_top = os.path.abspath('data/top.json')
    json_saver_top = JsonSaver(path_json_top, "w")
    json_saver_top.add_vacancy(top_vacancies)


if __name__ == "__main__":
    user_interaction()
