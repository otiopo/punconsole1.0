import os, colorama

os.system("clear")

with open("banner.txt", "r") as file:
  print(colorama.Fore.RED + file.read())
  file.close()