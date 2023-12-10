from utils import filter_data_list, read_json, sort_list_by_date


data_list = read_json()
data_list = filter_data_list(data_list)
print(sort_list_by_date(data_list))
