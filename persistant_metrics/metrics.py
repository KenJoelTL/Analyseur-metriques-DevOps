import json
from datetime import datetime


def getData(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
    end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M')
    database = {}
    f = open('./database.json')
    database = json.load(f)
    f.close()
    # print(database)
    sub_database = {}
    for date, record in database.items():
        date = datetime.strptime(date, '%Y-%m-%d %H:%M')
        if date > end_date:
            break
        if date >= start_date:
            sub_database[date.strftime('%Y-%m-%d %H:%M')] = record

    return sub_database


def print_formatted_datase(database):
    for date, record in database.items():
        print(date)
        for col_name, tasks in record.items():
            print("\t"+col_name)
            for task in tasks:
                print("\t"+"\t"+task['card_title'] +
                      ' - ' + task['created_at'])
