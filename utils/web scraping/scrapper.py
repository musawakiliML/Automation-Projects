import requests


try:
   r = requests.get("http://ip.jsontest.com/")
   print("response object", r)
   print("response text", r.text)
except requests.exceptions.RequestException as e:
   print("Error Message:", e)