import requests


def get_lat_lng(place_name):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': place_name,
        'format': 'json',
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        if data:
            latitude, longitude = float(data[0]['lat']), float(data[0]['lon'])
            return latitude, longitude
    return None


place_name = ''
result = get_lat_lng(place_name)

if result:
    print(f"Latitude: {result[0]}, Longitude: {result[1]}")
else:
    print(f"Could not find coordinates for {place_name}")
