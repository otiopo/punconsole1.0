import requests, sys

if len(sys.argv) > 2:
  print(requests.get(sys.argv[2]).text if "--youtuberedirect" in sys.argv else requests.get(sys.argv[2]).url)