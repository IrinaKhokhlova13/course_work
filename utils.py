import json
from datetime import datetime

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



def sort_list_by_date(data_list):
    '''
    Возвращает отсортированный список по полю date (дата), на выходе список из 5 элементов
    '''
    data_list = sorted(data_list, key=lambda x: x["date"], reverse=True)
    return data_list[:5]



def edit_date(date: str):
    '''
    Возвращает дату в нужном формате
    '''
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    date = datetime.strftime(date, "%d.%m.%Y")
    return date