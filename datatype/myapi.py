import requests
import json

data={}

timelineURL = "https://corona-api.com/timeline"

country = "https://corona-api.com/countries"

def get_timeline():
    data = requests.get(timelineURL).json()
    return data['data']

def get_country():
    data = requests.get(country).json()
    return data['data']

if __name__=="__main__":
    #data_test = get_data()

    print(data_test[0]['date'])
