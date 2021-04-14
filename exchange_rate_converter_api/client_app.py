from libs.OpenExchange import OpenExchangeClient
import requests

APP_ID = "*********"         #API ID from openexchange.org
client = OpenExchangeClient(APP_ID)         #create an object of your exchange client

usd_amount = 1000
gbp_amount = client.convert(usd_amount, "USD", "GBP")

print(f"${usd_amount} USD is equal to £{gbp_amount:.2f} GBP") #use the :.f in the format string to round to 2 decimal places