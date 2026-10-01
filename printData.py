import fetch_data

def formatTime(n):
    return f"{n//60:02}:{n%60:02}"

data = fetch_data.update()

for entry in data:
    for element in entry["departures"]:
        train_id = element["id"]
        departure_time = formatTime(element["departure"])
        stops_ahead =  " | ".join(element["via"])[:200]
        print(train_id + " "*(10-len(train_id)) + departure_time + " " + stops_ahead)