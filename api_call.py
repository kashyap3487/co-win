import requests
data=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=776&date=13-05-2021")
print(data)
