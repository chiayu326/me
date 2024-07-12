TODO: Reflect on what you learned this week and what is still unclear.

import json
import os
import requests

# 1

LOCAL = os.path.dirname(os.path.realpath(**file**)) # the context of this file
CWD = os.getcwd() # The curent working directory

# JASON file:

with open("data.json", "r") as file:
data = json.load(file)

# obtain information from a website:

r = requests.get(f"{in}url")  
if r.status_code == 200:
word = r.text
pyramid.append(word)

id = i
url = f"https://pokeapi.co/api/v2/pokemon/{id}"
r = requests.get(url)
if r.status_code == 200:
the_json = json.loads(r.text)

# Define the path to the gcode file and the output file

current_dir = os.path.dirname(os.path.realpath(**file**))
gcode_file_path = os.path.join(current_dir, "Trispokedovetiles(laser).gcode")
output_file_path = os.path.join(current_dir, "lasers.pew")

# load the file

with open(gcode_file_path, "r") as file:
gcode_content = file.read()
m10_p1_count = gcode_content.count("M10 P1")

# Write the count to the output file

with open(output_file_path, "w") as file:
file.write(str(m10_p1_count))
