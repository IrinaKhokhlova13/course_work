import json


def read_json():
    '''
    Возвращает список всей информации по операциям из файла json
    '''
    with open("operations.json", encoding="utf-8") as file:
        return json.load(file)