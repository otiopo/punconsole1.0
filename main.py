import time, random, threading, requests, colorama, getpass, socket, os

animation = r"\|/-"

print("Pun Console Is Loading Http Data...")
if os.name == "nt":
  print("We're not supporting windows on this version use wsl if you want to")
  exit()
isLoaded = False
timepassed = 0
def loadHttp():
  global isLoaded
  time.sleep(0.3)
  print("CHANGE LOG: " + str(requests.get("https://pconsoleapi.otiopo.repl.co/changelog").status_code))
  isLoaded = True
threading.Thread(target=loadHttp).start()
haspopped = False
haspopped2 = False
while isLoaded == False:
  if isLoaded == True:
    break
  timepassed += 1
  if timepassed > 8 and haspopped == False:
    print("PunConsole Is Taking Longer to Load Than Usual!")
    haspopped = True
  if timepassed > 19 and haspopped2 == False:
    print("PunConsole Is Not Loading, Check Your Internet connection. If your internet connection is ok then theres a problem with the servers!")
    haspopped2 = True
  for letter in animation:
    print("\r" + colorama.Fore.RED + letter + colorama.Style.RESET_ALL, end="\r")
    time.sleep(random.uniform(0.1, 0.4))
with open("banner.txt", "r") as file:
  print(colorama.Fore.RED + file.read())
  file.close()

while True:
  print(colorama.Fore.RED + "--(" + colorama.Fore.GREEN + "PConsole$" + colorama.Fore.CYAN + "[" + getpass.getuser()  + "]" + colorama.Fore.RED + ")")
  command = input("|_" + colorama.Fore.CYAN + socket.gethostbyname(socket.gethostname()) + colorama.Fore.RED + "$" + colorama.Fore.GREEN + socket.gethostname() + "> " + colorama.Style.RESET_ALL)
  if command != "" and command != " ":
    os.system("python3 cmds/" + command.split(" ")[0] + ".py " + command)