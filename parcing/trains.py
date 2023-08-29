import requests
from bs4 import BeautifulSoup
import prettytable as pt


def get_road(first_station, second_station):
    r = requests.get(url=f"https://poezdato.net/raspisanie-poezdov/{first_station}--{second_station}/")
    data = BeautifulSoup(r.text, "lxml")
    table = data.find("table")
    tbody = data.find("tbody")
    # Отправление | Прибытие | В пути
    arrival = table.find(class_="arrival").text.strip()
    dispatch = table.find(class_="dispatch").text.strip()
    time_way= table.find(class_="time_way").text.strip()
    # Создаем табицу 
    form_table = pt.PrettyTable([arrival,dispatch])
    tbody_tr = tbody.find_all("tr")
    #  Забираем данные с каждой строки таблицы
    for i in tbody_tr:
        all_arive_time = i.find_all(class_ ="_time")
        all_station_name= i.find_all(class_="small_font_station")
        for a,b in all_arive_time,all_station_name:
            arive_time= a.text.strip()
            station_name =b.text.strip()
            # print(f"{arive_time} | {station_name} |")
            form_table.add_row([arive_time , station_name])
        form_table.add_row(["", ""], divider=True)
    return form_table


    
