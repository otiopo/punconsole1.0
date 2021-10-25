import socket, requests, getmac, sys

localip = socket.gethostbyname(socket.gethostname())

print("Local IP: " + "Hidden" if "--hidelip" in sys.argv else "Local IP: " + localip + " (note this is a loopback address)" if  localip.startswith("172") else localip)
print("Public IP: " + "Hidden" if "--hidepip" in sys.argv else "Public IP: " + requests.get("http://ip-api.com/json").json()["query"])
print("MAC Address: " + "Hidden" if "--hidemac" in sys.argv else "MAC Address: " + getmac.get_mac_address())