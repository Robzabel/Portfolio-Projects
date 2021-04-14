import requests

APP_ID = "******************"         #API ID from openexchange.org
ENDPOINT = "https://openexchangerates.org/api/latest.json"          #The endpoint we are going to query

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")          #The API response will come back in json format
exchange_rates = response.json()['rates']           #Access the rates through calling the jsonfrom the response and retrieving all the values associated with the rates key

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates["GBP"]           #Convert $1000 into pound sterling

print(f"${usd_amount} USD is equal to £{gbp_amount} GBP")