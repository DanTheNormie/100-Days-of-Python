travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#to be added to the travel_log. 👇

def add_new_country(country,no_of_visits,list_of_cities_visited):
  
  travel_log.append({
    "country": country,
    "visits": no_of_visits,
    "cities": list_of_cities_visited
    })

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)