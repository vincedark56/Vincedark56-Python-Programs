# by VINCEDARK56

import re

user_message = input("Enter the RME pos copy:")

result = re.sub(r'[a-zA-Z].= ', '', user_message)
# I don't know a way to replace at one time
result = result.replace(",", "")
result = result.replace("{", "")
result = result.replace("}", "")

rsplit = result.split(" ")
remere_x = int(rsplit[0])
remere_y = int(rsplit[1])
remere_z = int(rsplit[2])

luanti_pos_x = remere_x - 32500
luanti_pos_y = remere_y - 32000
luanti_pos_z = remere_z - 7
print("Luanti position X =", luanti_pos_x,", Y =", luanti_pos_z,", Z =", -luanti_pos_y * 3)