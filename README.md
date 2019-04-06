# bs4WebScrape

Python Web Scrape

This allows you to run the command "python weather.py <zipcode>" in my OSX terminal and be returned 
the current weather in my area from weather.gov

To do this, I use the uszipcode module and its database to connect the entered zip code 
with its correct latitude and longitude coordinates. 

Then, a request is sent to the website for its content on those coordinates. 

The HTML is saved in an object to be properly parsed, using the beautifulSoup4 module. 

The data containing the current weather is extracted from its HTML tag, saved, and printed to the command line.

The code itself is very short and simple.
