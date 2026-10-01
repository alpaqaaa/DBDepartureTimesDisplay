import fetch_data
from datetime import datetime

def formatTime(n):
    return f"{n//60:02}:{n%60:02}"

def retrieveData():
    time = datetime.now()
    mins = 60*int(str(time.hour)) + int(str(time.minute))
    data = fetch_data.update()
    trains = []

    for entry in data:
        for train in entry["departures"]:
            if len(trains) >= 4:
                return trains
            if train["departure"] >= mins:
                trains.append(train)

    return trains