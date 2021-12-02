import requests
from bs4 import BeautifulSoup
import pandas as pd

r= requests.get('https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
c= r.content
l = []


soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div",{"class":"propertyRow"})

for item in all:
    d={}

    d["Address"] = item.find_all("span", {"class": "propAddressCollapse"})[0].text

    try:
        d["Area"] = item.find("span", {"class": "infoSqFt"}).find("b").text
    except:
        d["Area"] = None

    try:
        d["Beds"] = item.find("span", {"class": "infoBed"}).find("b").text
    except:
        d["Beds"] = None

    try:
        d["Full Bath"] = item.find("span", {"class": "infoValueFullBath"}).find("b").text
    except:
        d["Full Bath"] = None

    try:
        d["Half Bath"] = item.find("span", {"class": "infoValueHalfBath"}).find("b").text
    except:
        d["Half Bath"] = None

    d["Locality"] = item.find_all("span", {"class": "propAddressCollapse"})[1].text
    for column_group in item.find_all("div",{"class": "columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span",{"class": "featureGroup"}),column_group.find_all("span",{"class": "featureName"})):
            if "Lot Size" in feature_group.text:
                d["Lot Size"] = feature_name.text

    d["price"] = item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
    l.append(d)

df = pd.DataFrame(l)
df.to_csv("output.csv")