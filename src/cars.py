
import requests
from bs4 import BeautifulSoup
import pandas as pd
#url ="https://www.beforward.jp/stocklist/kmode=and/mfg_year_from=2018/mfg_year_to=2026/sar=steering/sortkey=n/steering=Right/tp_country_id=27"
#url="https://www.beforward.jp/stocklist/kmode=and/mfg_year_from=2018/mfg_year_to=2026/page="+str(i)+"/sar=steering/sortkey=n/steering=Right/tp_country_id=27"
#r = requests.get(url)
#print(r)
from bs4 import XMLParsedAsHTMLWarning
import warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
#soup = BeautifulSoup(r.text,"lxml")
#print(soup)
#results = soup.find_all("tr",class_="stocklist-row")
#print(len(results))
#print(results[0])
#print(results[0].find("p",class_="make-model").get_text())
#print(results[0].find("td",class_="basic-spec-col basic-spec-col-bordered mileage").get_text())
#print(results[0].find("td",class_="basic-spec-col basic-spec-col-bordered year").get_text())
#print(results[0].find("td",class_="basic-spec-col basic-spec-col-bordered engine").get_text())
#print(results[0].find("p",class_="vehicle-price").get_text())
#print(results[0].find("td",class_="basic-spec-col basic-spec-col-bordered trans").get_text())

Model =[]
Mileage =[]
Year =[]
Engine_size =[]
Price =[]
Transmission_type =[]

for i in range(2001,4001):
    url="https://www.beforward.jp/stocklist/kmode=and/mfg_year_from=2018/mfg_year_to=2026/page="+ str(i) +"/sar=steering/sortkey=n/steering=Right/tp_country_id=27"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    #print(soup)
    results = soup.find_all("tr",class_="stocklist-row")
    import time
    import random

    time.sleep(random.uniform(1,4))
#print(r)

    for result in results:
        try:
            Model.append(result.find("p",class_="make-model").get_text(strip= True))
        except:
            Model.append("n/a")
        try:
            Mileage.append(result.find("td",class_="basic-spec-col basic-spec-col-bordered mileage").get_text(strip =True))
        except:
            Mileage.append("n/a")
        try:
            Year.append(result.find("td",class_="basic-spec-col basic-spec-col-bordered year").get_text(strip = True))
        except:
            Year.append("n/a")
        try:
            Engine_size.append(result.find("td",class_="basic-spec-col basic-spec-col-bordered engine").get_text(strip = True))
        except:
            Engine_size.append("n/a")
        try:
            Price.append(result.find("p",class_="vehicle-price").get_text(strip=True))
        except:
            Price.append("n/a")
        try:
            Transmission_type.append(result.find("td",class_="basic-spec-col basic-spec-col-bordered trans").get_text(strip= True))
        except:
            Transmission_type.append("n/a")


car_prices_4000 = pd.DataFrame({
    "Model":Model,
    "Mileage":Mileage,
    "Year":Year,
    "Engine_size":Engine_size,
    "Price":Price,
    "Transmission_type":Transmission_type
})


car_prices_4000["Mileage"] = car_prices_4000["Mileage"].str.replace("Mileage", "", regex=False)
car_prices_4000["Year"] = car_prices_4000["Year"].str.replace("Year", "", regex=False)
car_prices_4000["Engine_size"] = car_prices_4000["Engine_size"].str.replace("Engine", "", regex=False)
car_prices_4000["Transmission_type"] = car_prices_4000["Transmission_type"].str.replace("Trans.", "", regex=False)

# remove extra spaces
car_prices_4000 = car_prices_4000.apply(
    lambda col: col.str.strip() if col.dtype == "object" else col
)


car_prices_4000["Model"] = (
    car_prices_4000["Model"]
    .str.replace("\n", " ", regex=False)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)
car_prices_4000.to_csv("car_prices_4000.csv",index=False)


#website ="https://www.beforward.jp/stocklist/kmode=and/mfg_year_from=2018/mfg_year_to=2026/page="+str(i)+"/sar=steering/sortkey=n/steering=Right/tp_country_id=27"



