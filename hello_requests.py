#
# hello_requests.py
#


# Installation: 'requests' in requirements.txt


import requests  


# The `requests` library allows you to send HTTP requests, for
# accessing web pages or web APIs.
# https://requests.readthedocs.io

# Weather API documentation 
# https://www.weather.gov/documentation/services-web-api

# National Weather Service (NWS) 
# https://www.weather.gov/

# NOAA 
# https://www.noaa.gov/


def main():

    # https://api.weather.gov/points/{latitude},{longitude}
    url = "https://api.weather.gov/points/34.0699142,-118.3294098"

    # Use the `get()` function to retrieve a webpage (GET request).

    response = requests.get(url)

    # Status code 200 is success.

    print("status_code:", response.status_code)
    print()

    if response.status_code != 200:
        print("Error.")
        return

    # The response from a webpage will generatlly be HTML.  The
    # response from a web API will usually be in JSON format, which
    # you can think of as a bunch of nested dictionaries.

    result_json = response.json()
    properties = result_json['properties']

    city = properties['relativeLocation']['properties']['city']
    forecast_url = properties['forecast']

    print("city:", city)
    print("forecast_url:", forecast_url)
    print()

    # Accessing the actual forecast requires a second GET request.

    response = requests.get(forecast_url)

    properties = response.json()['properties']
    periods = properties['periods']

    for period in periods:
        print(period['name'])
        print(period['detailedForecast'])
        print()


if __name__ == '__main__':
    main()
