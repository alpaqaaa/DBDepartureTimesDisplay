import requests, operator
import json, xmltodict
from datetime import datetime

# ------------ CUSTOMIZE HERE ------------

settings = {
    "station": "Offenbach Hbf",
}

# ----------------- DONE -----------------

station_ids = {
    "Offenbach Hbf": 8000349,
    "Frankfurt(Main)Hbf": 8000105
}

with open("headers.json") as f:
    headers = json.loads(f.read())

def formatTime(n):
    return f"{n//60:02}:{n%60:02}"

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
            data_sorted["departures"].append({
                "train_id": str(element["dp"]["@fb"]),
                "departure_time": 60*int(element["dp"]["@pt"][-4:-2]) + int(element["dp"]["@pt"][-2:]),
                "stops_ahead": element["dp"]["@ppth"].split("|")
            })

    data_sorted["departures"].sort(key=operator.itemgetter('departure_time'))
    return data_sorted

def update():
    time = datetime.now()
    date = f"{(time.year%100):02}" + f"{time.month:02}" + f"{time.day:02}"
    hour = time.hour
    if settings["station"] in station_ids:
        evaNo = station_ids[settings["station"]]
    else:
        evaNo = settings["station"]
    data = retrieveData(f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{evaNo}/{date}/{hour}")
    sorted_data = sortData(data)
    return sorted_data

data = update()

for element in data["departures"]:
    train_id = element["train_id"]
    departure_time = formatTime(element["departure_time"])
    stops_ahead =  " | ".join(element["stops_ahead"])[:200]
    print(train_id + " "*(10-len(train_id)) + departure_time + " " + stops_ahead)