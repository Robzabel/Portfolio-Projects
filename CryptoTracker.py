<<<<<<< HEAD
#!/usr/bin/env python3


import time                                                     #import time module for sleep timer and to check for turning the backlight off
import drivers                                                  #import the i2c library. Thanks to TheRaspberryPiGuy on YouTube
from coinbase.wallet.client import Client                       #import the coinbase client from the coinbase module
"""
Create the  Client Object
"""
api_key = ''                                                    #This information is provided when you create API keys on the coinbase website
api_secret = ''
client = Client(api_key, api_secret)                            #add the key and the secret to the client class to make an client object 

"""
Setup your objects 
"""
display = drivers.Lcd()                                         #create the display object from the drivers module
accounts = client.get_accounts()                                #use the client object to query the api for the accounts info which is recieved as a dictionary 
favourite = ["GRT", "NU", "OXT", "ZRX"]                         #Create a list of the Crypto that I want to be used 

"""
Main body of code
"""
try:                                                            #Encapsulate within a try/except block so you can easily stop the app
    while True:                                                 
        total = 0.00                                            #initialise the total variable so that it resets each loop
        for wallet in accounts.data:                            #iterate over the values of the dictionary key "data"
            if wallet['balance']['currency'] in favourite:      #use the favourites list to filter the results 
                display.lcd_display_string(f"{wallet['native_balance']['amount']} GBP of {wallet['balance']['currency']}", 1)   #print the information to the top line of the 16x2 LCD display
                price = client.get_spot_price(currency_pair = f"{wallet['balance']['currency']}-GBP")                           #Get the current sale price for each currency share 
                display.lcd_display_string(f"{float(price['amount']):.3f} per share", 2)                                        #Display the share price on the bottom line of the screen, formatted to 3 decimal places
                total += float(wallet['native_balance']['amount'])                                                              #Keep a running tally of the total
                time.sleep(7)                                   #pause the loop for 7 seconds
                display.lcd_clear()                             #Clear the screen so there are no left over characters displayed on the next iteration
        display.lcd_display_string(f"Crypto Portfolio", 1)      #Once the currency stats loop is complete print the portfolio total
        display.lcd_display_string(f"Total GBP {total}", 2)
        time.sleep(7)
        display.lcd_clear()                                     #clear any remaining characters and rtestart the loop
        t = time.localtime()                                    #create a time object
        current_time = time.strftime("%H", t)                   #pull the hour from the current time
        if int(current_time) > 20 or int(current_time) < 8:     #Check if the time is before 9PM
            display.lcd_backlight(0)                            #if its past 9PM or ealier than 8AM turn the backlight off on the display
        else:
            display.lcd_backlight(1)                            #If it is past 8PM but before 9PM keep the backlight on

except KeyboardInterrupt:                                       #If you wnat to stop the programme press CTRL + C
    print("Cleaning up")                                        #Let the user know the programme has finished and is clearing the screen
    display.lcd_clear()                                         #call the display method to clear the screen
=======
#!/usr/bin/env python3


import time                                                     #import time module for sleep timer and to check for turning the backlight off
import drivers                                                  #import the i2c library. Thanks to TheRaspberryPiGuy on YouTube
from coinbase.wallet.client import Client                       #import the coinbase client from the coinbase module
"""
Create the  Client Object
"""
api_key = ''                                                    #This information is provided when you create API keys on the coinbase website
api_secret = ''
client = Client(api_key, api_secret)                            #add the key and the secret to the client class to make an client object 

"""
Setup your objects 
"""
display = drivers.Lcd()                                         #create the display object from the drivers module
accounts = client.get_accounts()                                #use the client object to query the api for the accounts info which is recieved as a dictionary 
favourite = ["GRT", "NU", "OXT", "ZRX"]                         #Create a list of the Crypto that I want to be used 

"""
Main body of code
"""
try:                                                            #Encapsulate within a try/except block so you can easily stop the app
    while True: 
        t = time.localtime()                                    #create a time object
        current_time = time.strftime("%H", t)                   #pull the hour from the current time
        if int(current_time) > 20 or int(current_time) < 8:     #Check if the time is before 9PM or after 8am
            display.lcd_backlight(0)                            #if its past 9PM or ealier than 8AM turn the backlight off on the display
        else:                                                   #If it is past 8am and before 9pm run the code
            total = 0.00                                            #initialise the total variable so that it resets each loop
            for wallet in accounts.data:                            #iterate over the values of the dictionary key "data"
                if wallet['balance']['currency'] in favourite:      #use the favourites list to filter the results 
                    display.lcd_display_string(f"{wallet['native_balance']['amount']} GBP of {wallet['balance']['currency']}", 1)   #print the information to the top line of the 16x2 LCD display
                    price = client.get_spot_price(currency_pair = f"{wallet['balance']['currency']}-GBP")                           #Get the current sale price for each currency share 
                    display.lcd_display_string(f"{float(price['amount']):.3f} per share", 2)                                        #Display the share price on the bottom line of the screen, formatted to 3 decimal places
                    total += float(wallet['native_balance']['amount'])                                                              #Keep a running tally of the total
                    time.sleep(7)                                   #pause the loop for 7 seconds
                    display.lcd_clear()                             #Clear the screen so there are no left over characters displayed on the next iteration
            display.lcd_display_string(f"Crypto Portfolio", 1)      #Once the currency stats loop is complete print the portfolio total
            display.lcd_display_string(f"Total GBP {total}", 2)
            time.sleep(7)
            display.lcd_clear()                                     #clear any remaining characters and rtestart the loop

except KeyboardInterrupt:                                       #If you wnat to stop the programme press CTRL + C
    print("Cleaning up")                                        #Let the user know the programme has finished and is clearing the screen
    display.lcd_clear()                                         #call the display method to clear the screen
>>>>>>> 40f1b5d984f706167ee102180e6943eef1316be2
