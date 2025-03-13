import requests

x = requests.get('https://web.sabit.keenetic.pro/project_program1c/get_items.php?get_items_id=265')

print(x.text)

