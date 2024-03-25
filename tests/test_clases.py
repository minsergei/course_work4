import pytest
from src.saverjs import JsonSaver
from src.vacancy import Vacancy
from pathlib import Path


@pytest.fixture()
def test_json():
    path_json = Path(__file__).parent.joinpath('data_test/test_top.json')
    test_save = JsonSaver(path_json, "r+")
    data_test = test_save.read_file()
    return data_test, test_save


def test_sort_top_vacancy(test_json):
    Vacancy.cast_to_object_list(test_json[0])
    assert Vacancy.get_top(1) == [{'experience': 'От 1 года до 3 лет',
                                   'name': 'Продавец-консультант',
                                   'salary_from': 0,
                                   'salary_to': 60000,
                                   'snippet': 'консультирование посетителей по товару. - помощь в выборе '
                                              'товара. - размещение товара в торговом зале. - смена ценников. - '
                                              'работа в 1С. - ',
                                   'url': 'https://hh.ru/vacancy/93803891'}]


def test_delete_vacancy(test_json):
    test_json[1].delete_vacancy('Продавец в пекарню')
    data = test_json[1].read_file()
    assert len(data) == 4

# pytest --cov src --cov-report term-missing
