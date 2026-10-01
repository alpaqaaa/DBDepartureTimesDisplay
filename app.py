from tkinter import *
import fetch_data, json

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

headers = {
    "title": canvas.create_text(5, 5, anchor="nw", font=styles["large"], fill="#ffffff", text=settings["station"]),
    "id": canvas.create_text(5, 25, anchor="nw", font=styles["small"], fill="#ffffff", text="Zug"),
    "departure": canvas.create_text(55, 25, anchor="nw", font=styles["small"], fill="#ffffff", text="Abfahrt"),
    "destination": canvas.create_text(135, 25, anchor="nw", font=styles["small"], fill="#ffffff", text="Ziel"),
    "via": canvas.create_text(300, 25, anchor="nw", font=styles["small"], fill="#ffffff", text="via")
}

def updateScreen():
    return

root.mainloop()