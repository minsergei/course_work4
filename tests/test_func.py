import pytest
from pathlib import Path
from src.saverjs import JsonSaver
from src.func import get_filter_vacancies, get_ranged_vacancies


@pytest.fixture()
def test_json():
    path_json = Path(__file__).parent.joinpath('data_test/test_top.json')
    test_save = JsonSaver(path_json, "r+")
    data_test = test_save.read_file()
    return data_test, test_save


def test_raise_get_ranged_vacancies(test_json):
    with pytest.raises(TypeError):
        get_ranged_vacancies(test_json[0], '423423wsfsf')


def test_get_ranged_vacancies(test_json):
    assert get_ranged_vacancies(test_json[0], '70000 - 80000') == [{'experience': 'Нет опыта',
                                                                    'name': 'Продавец-консультант в шоу-рум ( выплаты ежедневно)',
                                                                    'salary_from': 55000,
                                                                    'salary_to': 95000,
                                                                    'snippet': 'Консультации покупателей и продажа одежды(работа без кассы). '
                                                                               'Помощь в примерке. Работа с ценниками, выкладка товара, '
                                                                               'отпаривание одежды. ',
                                                                    'url': 'https://hh.ru/vacancy/94640824'}]


def test_get_filter_vacancies(test_json):
    assert get_filter_vacancies(test_json[0], ['размещать']) == [{'experience': 'Нет опыта',
                                                                  'name': 'Специалист пункта выдачи заказов',
                                                                  'salary_from': 51000,
                                                                  'salary_to': 57000,
                                                                  'snippet': 'Выдавать интернет-заказы и консультировать клиентов. Принимать и '
                                                                             'размещать товар в магазине. Проверять работоспособность товара. '
                                                                             'Работать с кассой.',
                                                                  'url': 'https://hh.ru/vacancy/95116508'}]