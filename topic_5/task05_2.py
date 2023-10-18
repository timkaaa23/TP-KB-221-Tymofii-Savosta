import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")

value = float(input('Уведіть кількість грошей: '))
value = round(value, 2)
currency = input('Оберіть валюту "USD", "EUR" чи "PLN": ')

for elem in response.json():
    if elem['cc'] == currency:
    	result = value * float(elem['rate'])
    	result = round(result, 2) 
    	print(f'{value} {currency} = {result} UAH')
    	break