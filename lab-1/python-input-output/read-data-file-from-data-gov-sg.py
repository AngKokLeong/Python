import requests

r = requests.get('https://data.gov.sg/api/action/datastore_search?resource_id=d_d6921f812624c2b1bb1d68269354dc71')

#print(r.json()['result']['records'])

dataset_list: list[list[str]] = []

average_daily_passenger_journeys_list: list[int] = []

for item in r.json()['result']['records']:
    
    dataset_list.append([item['_id'], item["year"], item["average_daily_passenger_journeys"], item["average_journey_distances"]])
    average_daily_passenger_journeys_list.append(item["average_daily_passenger_journeys"])

average_daily_passenger_journeys_list.sort()

lowest_average_daily_passenger_journey: int = average_daily_passenger_journeys_list[0]
highest_average_daily_passenger_journey: int = average_daily_passenger_journeys_list[-1]

for item in dataset_list:

    if int(item[2]) == int(lowest_average_daily_passenger_journey):
        print("The minimum number of journeys happened in year {0:s} with {1:s} journeys".format(item[1], item[2]))
    
    if int(item[2]) == int(highest_average_daily_passenger_journey):
        print("The maximum number of journeys happened in year {0:s} with {1:s} journeys".format(item[1], item[2]))