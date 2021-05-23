import numpy as np
import pandas as pd
import mechanicalsoup
from bs4 import BeautifulSoup
import re
import csv

#go to and login to website
 
browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)

browser.open("https://www.pararius.com/english")
browser.follow_link("login")

form = browser.select_form()

browser["email"] = "cm.calmus@gmail.com"
browser["password"] = "Pineapple2021"

form.print_summary()

browser.submit_selected()

# follow link to amsterdam rentals
browser.follow_link("/apartments/amsterdam")
print(browser.get_url())

bs4 = browser.get_current_page()

#get text from all advertisements & convert to csv
ads = bs4.find_all("li", class_ = "search-list__item search-list__item--listing")

df = pd.DataFrame(columns = ['Address', 'Postcode', 'Size in m²', 'Rooms', 'Prize in €'])
for ad in ads:
    new_item = ad.get_text()
    start_address = new_item.find("Apartment")
    end_address = new_item.find("Amsterdam") - 9
    full_address = new_item [start_address:end_address]
    end_postcode = new_item.find("Amsterdam")
    start_postcode = end_postcode - 9 
    full_postcode = new_item[start_postcode:end_postcode]
    end_size = new_item.find("Living area")
    start_size = end_size - 7
    full_size = new_item[start_size +1 :end_size -3]
    end_rooms = new_item.find("Rooms")
    start_rooms = end_rooms - 3
    full_rooms = new_item[start_rooms +1 :end_rooms - 1]
    end_prize = new_item.find("per month")
    start_prize = end_prize - 8
    full_prize = new_item[start_prize + 2:end_prize -1]
    summary = [[full_address, 
        full_postcode, 
        full_size, 
        full_rooms, 
        full_prize
        ]]
    df = df.append(pd.DataFrame(summary, columns = ['Address', 'Postcode', 'Size in m²', 'Rooms', 'Prize in €']))



#for all 85 pages
current_value = 2
while current_value <= 84:
    new_link = "/page-" + str(current_value) 
    browser.follow_link(new_link)
    bs4 = browser.get_current_page()
    ads = bs4.find_all("li", class_ = "search-list__item search-list__item--listing")
    for ad in ads:
        new_item = ad.get_text()
        start_address = new_item.find("Apartment")
        end_address = new_item.find("Amsterdam") - 9
        full_address = new_item [start_address:end_address]
        end_postcode = new_item.find("Amsterdam")
        start_postcode = end_postcode - 9 
        full_postcode = new_item[start_postcode:end_postcode]
        end_size = new_item.find("Living area")
        start_size = end_size - 7
        full_size = new_item[start_size +1 :end_size -3]
        end_rooms = new_item.find("Rooms")
        start_rooms = end_rooms - 3
        full_rooms = new_item[start_rooms +1:end_rooms -1]
        end_prize = new_item.find("per month")
        start_prize = end_prize - 8
        full_prize = new_item[start_prize +2:end_prize -1]
        summary = [[full_address, 
            full_postcode, 
            full_size, 
            full_rooms, 
            full_prize
            ]]
        df = df.append(pd.DataFrame(summary, columns = ['Address', 'Postcode', 'Size in m²', 'Rooms', 'Prize in €']))#
    current_value += 1

df.to_csv('pararius_scraped.csv')
print(df.head())

#was alternative: 
# current_value = 2
#while current_value <= 80:
#    new_link = "/page-" + str(current_value) 
#    browser.follow_link(new_link)
#    bs4 = browser.get_current_page()
#    ads = bs4.find_all("li", class_ = "search-list__item search-list__item--listing")
#    with open('pararius_scraped.csv', 'w', newline = '') as csvfile:
#        writer = csv.writer(csvfile)
#        for ad in ads:
#            ....
#            writer.writerow(summary)
#    current_value += 1
# .....