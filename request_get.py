import requests

x = requests.get('http://erlan.pro/project_program1c/get_items.php?get_items_id=265')

print(x.text)

