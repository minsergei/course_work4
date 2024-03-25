import pytest
from src.parser_hh import Parser
from src.saverjs import JsonSaver
from pathlib import Path


@pytest.fixture()
def test():
    path_json = Path(__file__).parent.joinpath('data_test/start_data.json')
    save_json = JsonSaver(path_json, "w")
    start_data = save_json.read_file()
    pars = Parser(start_data)
    vacancy = pars.get_pars()
    return vacancy


def test_parser(test):
    assert test[0]['salary_from'] == 0
    assert test[0]['salary_to'] == 95000


def test_add_to_json(test):
    path_json = Path(__file__).parent.joinpath('data_test/save_json.json')
    save_json = JsonSaver(path_json, "w")
    save_json.add_vacancy(test)
    save_json2 = JsonSaver(path_json, "r+")
    save_json2.add_vacancy(test)
    assert len(save_json.read_file()) == 8
