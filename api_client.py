import requests
from requests.exceptions import RequestException, HTTPError

class GetAddressAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_addresses(self, postcode):
        try:
            url = f"https://api.getAddress.io/find/{postcode}?api-key={self.api_key}"
            response = requests.get(url, timeout=10)  # Add a timeout
            response.raise_for_status()  # Check for HTTP errors
            return response.json()['addresses']
        except HTTPError as e:
            print(f"HTTP error: {e.response.status_code}")
            return None
        except RequestException as e:
            print(f"Request error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
