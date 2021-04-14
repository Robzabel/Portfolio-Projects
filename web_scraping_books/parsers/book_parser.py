import re
from locators.book_locators import BookLocators


class BookParser:
    """
    A Class to take in a HTML page and find properties of an item on it.
    """
    RATINGS = {
        'One' : 1,
        'Two' : 2,
        'Three': 3,
        'Four' : 4,
        'Five': 5    }


    def __init__(self, parent):
        self.parent = parent                         #An init function that takes in a page of HTML, parses it and stores it in the soup variable

    def __repr__(self):
        return f'<Book {self.name}, £{self.price} ({self.rating} stars)>'
    @property
    def name(self):                                           #creating a function to search based on CSS locators    
        locator = BookLocators.NAME_LOCATOR                     #You could create a variable to hold the string of tags to traverse
        item_link = self.parent.select_one(locator)     #or you can add the string straight to the select_one function. A space in the string signifies the next child tag to enter, the dot signifies an attribute to define the tag
        item_name = item_link.attrs.get('title')                    #once you have the tag stored as the item_link you can either use the attrs[''] dictionary key or the .get method to find attibrtes to return
        return (item_name)

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']          #This function searches for the item link so the attribute is called on the locator straight away after finding it
        return (item_link)

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR            #Finds an article tag wit hthe attribute 'product_pod' then finds a P tag with the attribute 'price_color'
        item_price = self.parent.select_one(locator).string                #uses price_color as a dictionary key to return the value that it represents in string format "£51.77"
        pattern = '£([0-9]+\.[0-9]+)'                               #breaks the price into 2 groups. the £ sign and the numbers are group 0 and the 51.77 on its own is group 1 becasue of how the brackets have been used
        matcher = re.search(pattern, item_price)                    #matches the pattern to the price
        return (float(matcher.group(1)))                              #Prints the price in float form without the £ so we can perform calculations on it 

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR             # finds the P tag that has the star-rating attribute in the article tag with the product_pod attribute
        star_rating_tag = self.parent.select_one(locator)                  #stores the star rating tag into the variable
        classes = star_rating_tag.attrs['class']                    #pulls the classes from the star rating tagged Paragraph. this will produce ['start-rating', 'Three'] because they are the two classes. because we cannot tell which way round they will be stored in the list, we cant use the index number to select them
        rating_classes = [r for r in classes if r != 'star-rating']     #We now need to find the rating attribute which is 'Three' so this seperates the two classes
        rating_number =  BookParser.RATINGS.get(rating_classes[0])  #now we match the string representation of the number to the int value by calling the RATINGS dictionary
        return rating_number                                        #Return the intager of the rating
