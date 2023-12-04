from database import PostcodeDatabase
from api_client import GetAddressAPI
from dotenv import load_dotenv
import os

def main():
    load_dotenv()  # Load environment variables

    db_uri = os.getenv('DATABASE_URI')
    api_key = os.getenv('API_KEY')

    db = PostcodeDatabase(db_uri)
    api_client = GetAddressAPI(api_key)

    while True:
        postcode = input("Enter a postcode (or 'exit' to quit): ").strip()
        if postcode.lower() == 'exit':
            break

        result = db.find_postcode(postcode)
        if result and (datetime.now() - result['last_accessed']).seconds < 86400:
            addresses = result['addresses']
        else:
            addresses = api_client.get_addresses(postcode)
            db.update_postcode(postcode, addresses)

        for address in addresses:
            print(address)

if __name__ == "__main__":
    main()
