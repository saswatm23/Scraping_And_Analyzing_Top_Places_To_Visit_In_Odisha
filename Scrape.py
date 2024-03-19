from bs4 import BeautifulSoup
import html5lib
import requests
import re
import pandas as pd


try:
    source = requests.get("https://www.holidify.com/state/odisha/top-destinations-places-to-visit.html")
    source.raise_for_status()
    soup = BeautifulSoup(source.text,'html5lib')
    contents = soup.find('div',class_="row no-gutters d-flex negative-margin-mobile").find_all('div',class_="col-12 col-md-6 pr-md-3")
    
    loc = []
    rate = []
    desc = []
    
    for content in contents:
        location = content.find('h3')
        loc.append(location.text.split(".")[1])
        ratings = content.find('span',class_="rating-badge")
        rate.append(ratings)
        description = content.find('p',class_='card-text')
        desc.append(description.text)

    DF = pd.DataFrame({"Place":loc,"Description":desc,"Rating":rate})
    #Converting the column to string type so that we could extract ratings
    DF['Rating'] = DF['Rating'].astype(str)
    # Function to extract rating from HTML code
    def extract_rating(html_code):
        pattern = r'<b>(\d+\.\d+)</b>'
        match = re.search(pattern, html_code)
        if match:
            return match.group(1)
        else:
            return None

    # Apply the function to the column containing HTML code
    DF['Rating'] = DF['Rating'].apply(extract_rating)



    print(DF)    
    DF.to_csv(r"C:\Users\saswa\OneDrive\Desktop\DBDA\Projects\Scraping_And_Analyzing_Top_Places_To_Visit_In_Odisha\tourism.csv")

    
except Exception as e :
    print(e)