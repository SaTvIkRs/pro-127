from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'

browser = webdriver.Chrome('D:/Setup/chromedriver_win32/chromedriver.exe')
browser.get(start_url)

scarped_data = []

def scarpe():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs={"class": "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    # Get data from <td> 
    for row in table_rows:
        table_cols = row.find_all('td')

        temp_list = []

        for col_data in table_cols:
            # Print Only columns textual data using ".text" property 
            data = col_data.text.strip()
            temp_list.append(data)

        # Append data to star data list 
        scarped_data.append(temp_list)

# Call the function to populate scarped_data
scarpe()

stars_data = []

for i in range(0, len(scarped_data)):
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum] 
    stars_data.append(required_data)

headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']

# Fix the typo in the following line
star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")
