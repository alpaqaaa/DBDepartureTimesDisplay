import api

def formatTime(n):
    return f"{n//60:02}:{n%60:02}"

data = api.update()

for element in data["departures"]:
    train_id = element["train_id"]
    departure_time = formatTime(element["departure_time"])
    stops_ahead =  " | ".join(element["stops_ahead"])[:200]
    print(train_id + " "*(10-len(train_id)) + departure_time + " " + stops_ahead)