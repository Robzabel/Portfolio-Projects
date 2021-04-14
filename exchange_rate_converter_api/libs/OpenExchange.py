import requests
from cachetools import cached, TTLCache


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    @property #Make this aproperty as it returns the requested JSON as the object variable latest
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json() #this only extracts the JSON from the request and doesnt worry about the response

    def convert(self, from_amount, from_currency, to_currency): #take in the arguments for what you want to convert
        rates = self.latest['rates']  #call the latest property and find the rates key in the dictionary
        to_rate = rates[to_currency] #find the currency you want in the list
        if from_currency == "USD":  #the currency will be USD 90% of the time but best to check
            return from_amount * to_rate    #times the currrency by the exchange rate to give the amout of money in the new currency
        else:  #if it is not in USD
            from_in_usd = from_amount / rates[from_currency] #to work out the base ammount of money, you need to divide it from the current currency
            return from_in_usd * to_rate # now you have the base currency you can multiply it by the exchange rate to get the correct figure
