import requests

class GetAddressAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_addresses(self, postcode):
        url = f"https://api.getAddress.io/find/{postcode}?api-key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['addresses']
        else:
            response.raise_for_status()
