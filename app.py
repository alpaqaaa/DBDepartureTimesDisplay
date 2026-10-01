from tkinter import *
import stringify_data, json

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

root = Tk()
root.geometry("512x128")
root.title(settings["station"])

canvas = Canvas(bg="#0000ff")
canvas.place(x=0, y=0, width=512, height=128)

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

for x in range(20):
    txt_element = canvas.create_text(headers_x_values[x%4], x//4 * 20 + 45, anchor="nw", font=styles["small"], fill="#ffffff", text="-")
    content.append(txt_element)

def updateScreen():
    trains = stringify_data.retrieveData()

    for train in enumerate(trains):
        canvas.itemconfig(content[4*train[0]], text=train[1]["id"])
        canvas.itemconfig(content[4*train[0]+1], text=formatTime(train[1]["departure"]))
        canvas.itemconfig(content[4*train[0]+2], text=train[1]["destination"])
        canvas.itemconfig(content[4*train[0]+3], text=train[1]["via"])

    root.after(30000, updateScreen)

updateScreen()

root.mainloop()