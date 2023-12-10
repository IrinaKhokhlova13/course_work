from utils import filter_data_list, read_json, sort_list_by_date, edit_date, hide_account_number


#data_list = read_json()
#data_list = filter_data_list(data_list)
#print(sort_list_by_date(data_list))

#print(edit_date("2019-07-03T18:35:29.512364"))

print(hide_account_number("Счет 64686473678894779589"))
print(hide_account_number("Maestro 1596837868705199"))
print(hide_account_number(""))