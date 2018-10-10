from __future__ import print_function
import twitter
import requests
from passwords import TWITTER_CONSUMER_KEY_PASS, TWITTER_CONSUMER_SECRET_PASS, TWITTER_ACCESS_TOKEN_KEY_PASS, TWITTER_ACCESS_TOKEN_SECRET_PASS
import time
import argparse


# File that gets and prints the cursor
CONSUMER_KEY = TWITTER_CONSUMER_KEY_PASS
CONSUMER_SECRET = TWITTER_CONSUMER_SECRET_PASS
ACCESS_TOKEN = TWITTER_ACCESS_TOKEN_KEY_PASS
ACCESS_TOKEN_SECRET = TWITTER_ACCESS_TOKEN_SECRET_PASS


# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


def get_bios(all_ids_file):
    bio_list = []

    with open(all_ids_file, 'r') as file:
        for line in file:
            fof_ids = line.split(',')

            with open('Bios.txt', 'wb') as f:
                for id in fof_ids:
                    print(id)

                    try:
                        bio = api.GetUser(user_id=id, include_entities=False).description
                        print(bio)
                        bio_list.append(bio)
                        time.sleep(.1)

                    except (requests.ConnectionError):
                        print("No Internet")

                    else:
                        f.write(bio_list)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('FoFIDs', type=str)
    args = argparser.parse_args()
    all_ids = args.FoFIDs
    get_bios(all_ids)