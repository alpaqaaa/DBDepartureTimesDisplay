import requests, operator
import json, xmltodict
from datetime import datetime, timedelta

with open("settings.json") as f:
    settings = json.loads(f.read())

with open("headers.json") as f:
    headers = json.loads(f.read())

with open("ibnr_lookup.json") as f:
    ibnrs = json.loads(f.read())

with open("name_lookup.json") as f:
    names = json.loads(f.read())

def retrieveData(url):
    response = requests.get(url, headers=headers)
    data = xmltodict.parse(response.text)
    return data

def sortData(data):
    data_sorted = {
        "station_name": data["timetable"]["@station"],
        "departures": []
    }

    for element in data["timetable"]["s"]:
        if "dp" in element:
            element_data = {
                "id": str(element["dp"]["@fb"]),
                "departure": 60*int(element["dp"]["@pt"][-4:-2]) + int(element["dp"]["@pt"][-2:]),
                "destination": "",
                "via": element["dp"]["@ppth"].split("|")
            }
            element_data["destination"] = element_data["via"][-1]
            data_sorted["departures"].append(element_data)

    data_sorted["departures"].sort(key=operator.itemgetter("departure"))
    return data_sorted

def update():
    times = [datetime.now(), datetime.now() + timedelta(hours=1)]

    sorted_data = []

    for time in times:
        date = f"{(time.year%100):02}" + f"{time.month:02}" + f"{time.day:02}"
        hour = time.hour
        if settings["station"] in ibnrs:
            ibnr = ibnrs[settings["station"]]
        else:
            ibnr = settings["station"]
        data = retrieveData(f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{ibnr}/{date}/{hour}")
        sorted_data.append(sortData(data))
    
    return sorted_data