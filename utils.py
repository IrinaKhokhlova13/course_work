import json


def read_json():
    '''
    Возвращает список всей информации по операциям из файла json
    '''
    with open("operations.json", encoding="utf-8") as file:
        return json.load(file)


def filter_data_list(data_list):
    '''
    Возвращает отфильтрованный список по полю state со значением EXECUTED
    '''
    list=[]
    for i in data_list:
        if i != {}:
            if i["state"] == "EXECUTED":
                list.append(i)
            else:
                continue
        else:
            continue
    return list