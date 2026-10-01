from tkinter import *
import stringify_data, json, time

# ----- SETUP -----

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480

# -----------------

max_nr = (WINDOW_HEIGHT - 45) // 20

def formatTime(n):
    try:
        int(n)
    except:
        raise SyntaxError("Number expected.")
    return f"{n//60:02}:{n%60:02}"

styles = {
    "large": ("Bahnschrift", 12),
    "medium": ("Bahnschrift", 10),
    "small": ("Bahnschrift", 8)
}

with open("settings.json") as f:
    settings = json.loads(f.read())

with open("name_lookup.json") as f:
    names = json.loads(f.read())

if settings["station"] in names:
    settings["station"] = names[settings["station"]]

root = Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.title(settings["station"])

canvas = Canvas(bg="#0000ff")
canvas.place(x=0, y=0, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

headers_x_values = {
    0: 5,
    1: 75,
    2: 155,
    3: 310,
}

headers = {
    "title": canvas.create_text(headers_x_values[0], 5, anchor="nw", font=styles["large"], fill="#ffffff", text=settings["station"]),
    "id": canvas.create_text(headers_x_values[0], 25, anchor="nw", font=styles["medium"], fill="#ffffff", text="Zug"),
    "departure": canvas.create_text(headers_x_values[1], 25, anchor="nw", font=styles["medium"], fill="#ffffff", text="Abfahrt"),
    "destination": canvas.create_text(headers_x_values[2], 25, anchor="nw", font=styles["medium"], fill="#ffffff", text="Ziel"),
    "via": canvas.create_text(headers_x_values[3], 25, anchor="nw", font=styles["medium"], fill="#ffffff", text="via")
}

content = []

for x in range(4*max_nr):
    txt_element = canvas.create_text(headers_x_values[x%4], x//4 * 20 + 45, anchor="nw", font=styles["small"], fill="#ffffff", text="")
    content.append(txt_element)

def updateScreen():
    trains = stringify_data.retrieveData(max_nr)

    for train in enumerate(trains):
        canvas.itemconfig(content[4*train[0]], text=train[1]["id"])
        canvas.itemconfig(content[4*train[0]+1], text=formatTime(train[1]["departure"]))
        canvas.itemconfig(content[4*train[0]+2], text=train[1]["destination"])
        canvas.itemconfig(content[4*train[0]+3], text=" | ".join(train[1]["via"]))

    seconds_until_next_minute = 61 - (time.time() % 60)
    root.after(int(seconds_until_next_minute * 1000), updateScreen)

updateScreen()

root.mainloop()