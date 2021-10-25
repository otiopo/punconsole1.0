import socket, sys

if len(sys.argv) > 2:
  addr = socket.gethostbyname(sys.argv[2])
  print("IP Addr: " + addr)
  print("DNS Records: " + socket.gethostbyaddr(addr)[0])