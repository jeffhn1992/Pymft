import re

file_open = open("mujir.txt")

prayer_text = file_open.read()

format_adjective1 = r"Glory be to You O (.+)!.*"
format_adjective2 = r"Glory be to You O .+! Exalted are You O (\w+?)!"

list_adj1 = re.findall(format_adjective1, prayer_text)
list_adj2 = re.findall(format_adjective2, prayer_text)

print(len(list_adj2))