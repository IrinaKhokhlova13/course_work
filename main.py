from utils import read_json, filter_data_list, sort_list_by_date, edit_date, hide_account_number


data_list = read_json()
data_list = filter_data_list(data_list)
data_list = sort_list_by_date(data_list)

for operation in data_list:
    #Вывод даты в правильно формате и типа операции
    print(f"{edit_date(operation['date'])} {operation['description']}")

    #Вывод информации номера карты(если он есть), номера счета(если он есть) или Оплата наличными
    if "from" in operation and "to" in operation:
        print(f"{hide_account_number(operation['from'])} -> {hide_account_number(operation['to'])}")
    elif "from" not in operation and "to" in operation:
        print(f"{hide_account_number('')} -> {hide_account_number(operation['to'])}")
    elif "from" in operation and "to" not in operation:
        print(f"{hide_account_number(operation['from'])} -> {hide_account_number('')}")
    else:
        print(hide_account_number(""))

    #Вывод суммы и валюты
    print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
    print("\n")

