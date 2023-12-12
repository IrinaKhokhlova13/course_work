import utils
import pytest

@pytest.fixture
def list(): # имя фикстуры любое
    return [{
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
        "amount": "41096.24",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
},
{
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
        "amount": "67314.70",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
}
]

date_list = [{"date": "2018-09-12T21:27:25.241689"}, {"date": "2019-12-08T22:46:21.935582"}]
date_format = "2019-12-08T22:46:21.935582"

account_number_1 = "Visa Platinum 1246377376343588"
account_number_2 = "Счет 14211924144426031657"



def test_filter_data_list(list):
    assert utils.filter_data_list([]) == []
    assert utils.filter_data_list(list) == [{"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582", "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}}, "description": "Открытие вклада", "to": "Счет 90424923579946435907"}]
    assert utils.filter_data_list([{}]) == []

def test_sort_list_by_date():
    assert utils.sort_list_by_date([]) == []
    assert utils.sort_list_by_date(date_list) == [{"date": "2019-12-08T22:46:21.935582"}, {"date": "2018-09-12T21:27:25.241689"}]


def test_edit_date():
    assert utils.edit_date(date_format) == "08.12.2019"


def test_hide_account_number():
    assert utils.hide_account_number(account_number_1) == "Visa Platinum  1246 37** **** 3588"
    assert utils.hide_account_number(account_number_2) == "Счет **1657"
    assert utils.hide_account_number("") == "Наличные средства"