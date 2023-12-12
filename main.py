from utils import read_json, filter_data_list, sort_list_by_date, edit_date, hide_account_number


data_list = read_json()
data_list = filter_data_list(data_list)
data_list = sort_list_by_date(data_list)

for i in data_list:
    #Вывод даты в правильно формате и типа операции
    print(f"{edit_date(i['date'])} {i['description']}")

    #Вывод информации номера карты(если он есть), номера счета(если он есть) или Оплата наличными
    if "from" in i and "to" in i:
        print(f"{hide_account_number(i['from'])} -> {hide_account_number(i['to'])}")
    elif "from" not in i and "to" in i:
        print(f"{hide_account_number('')} -> {hide_account_number(i['to'])}")
    elif "from" in i and "to" not in i:
        print(f"{hide_account_number(i['from'])} -> {hide_account_number('')}")
    else:
        print(hide_account_number(""))

    #Вывод суммы и валюты
    print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
    print ("\n")

