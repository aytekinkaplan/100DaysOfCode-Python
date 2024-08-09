import folium
import tkinter as tk
from tkinter import Frame
from tkinterhtml import HtmlFrame
import os

# 1. Create a Folium map
m = folium.Map(location=[38.58, -99.09], zoom_start=6)
folium.TileLayer(
    tiles='http://tile.stamen.com/terrain/{z}/{x}/{y}.png',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.',
    name='Stamen Terrain'
).add_to(m)
m.save("map.html")

# 2. Create a Tkinter GUI window
root = tk.Tk()
root.title("Map Viewer")

# 3. Create a Frame to hold the HTML content
frame = Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# 4. Create an HtmlFrame to display the HTML content
html_frame = HtmlFrame(frame, horizontal_scrollbar="auto")
html_frame.pack(fill=tk.BOTH, expand=True)

# 5. Load the HTML file content into the HtmlFrame
with open("map.html", "r", encoding="utf-8") as file:
    html_content = file.read()
html_frame.set_content(html_content)

# 6. Start the GUI event loop
root.mainloop()
