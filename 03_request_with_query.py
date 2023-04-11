import requests

payload = {"key1":"value1" ,"key2":"value2"}
r = requests.get("https://httpbin.org/get", params=payload)
print(r.json())
#  the above line as same as doing "https://httpbin.org/get1?key1=value1&key2=value2



