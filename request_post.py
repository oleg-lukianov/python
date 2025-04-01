import requests

url = 'http://erlan.pro/project_program1c/insert.php'

myobj = {"fop":"Dimon","clock":"1741891161","address":"Prospect","summa":"700","send":"Save"}

x = requests.post(url, json = myobj)

print(x.text)

