from database import PostcodeDatabase
from api_client import GetAddressAPI
from dotenv import load_dotenv
import os
import re
from datetime import datetime

def uk_postcode_format(postcode):
    # UK postcode regex pattern
    pattern = r'^[A-Z]{1,2}[0-9R][0-9A-Z]? ?[0-9][A-Z]{2}$'
    return re.match(pattern, postcode, re.IGNORECASE)

def main():
    load_dotenv()  # Load environment variables

    db_uri = os.getenv('DATABASE_URI')
    api_key = os.getenv('API_KEY')

    if not db_uri or not api_key:
        print("Database URI or API Key is not set. Please check your environment variables.")
        return

    db = PostcodeDatabase(db_uri)
    api_client = GetAddressAPI(api_key)

    while True:
        postcode = input("Enter a postcode (or 'exit' to quit): ").strip()
        if postcode.lower() == 'exit':
            break

        if not uk_postcode_format(postcode):
            print("Invalid postcode format. Please enter a valid postcode.")
            continue

        try:
            result = db.find_postcode(postcode)
            if result and (datetime.now() - result['last_accessed']).seconds < 86400:
                addresses = result['addresses']
            else:
                addresses = api_client.get_addresses(postcode)
                if addresses:
                    db.update_postcode(postcode, addresses)
                else:
                    print("Failed to fetch addresses from the API.")
                    continue

            for address in addresses:
                print(address)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
