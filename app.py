import requests
import json
from os import system
# import termcolors (for upcoming update)

while True:
    try:
        # getting and printing worldwide info
        print("Loading...")
        
        r = requests.get("https://disease.sh/v3/covid-19/all")
        r = r.text
        info = json.loads(r)
        
        system('clear')
        print(f"""
        Global Info:
        Total Cases: {info["cases"]}
        Active Cases: {info["active"]}
        Total Deaths: {info["deaths"]}
        """)

        # Contry-wise info
        country = input("Enter the name of the country => ").lower()
        print("Loading...")
        
        r = requests.get(f"https://disease.sh/v3/covid-19/countries/{country}")
        r = r.text
        info = json.loads(r)
        
        try:
            system('clear')
            print(f"""
            {country} info:
            Total Cases: {info["cases"]}
            Active Cases: {info["active"]}
            Total Deaths: {info["deaths"]}
            """)
        except KeyError:
            print("The country doesn't exist! Check if there's a typo")

        input("Press Enter to continue")
    
    except KeyboardInterrupt:
        system('clear')
        print("BYEE!!")
        exit()
