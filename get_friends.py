from __future__ import print_function
import twitter
from passwords import TWITTER_CONSUMER_KEY_PASS, TWITTER_CONSUMER_SECRET_PASS, TWITTER_ACCESS_TOKEN_KEY_PASS, TWITTER_ACCESS_TOKEN_SECRET_PASS
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

# TODO: figure out how to take in the user's screenname from the command line
# Parse command line arguments
#argparser = argparse.ArgumentParser()
#argparser.add_argument('screen_name', type=str)
#args = argparser.parse_args()
#screen_name = args.screen_name

# TODO - maybe refactor this code so that the writing only occurs once
def get_friend_ids(screen_name):
    friend_ids = []

    with open('FriendIDs.txt', 'w') as f:
        try:
            friends = api.GetFriendIDs(screen_name)
            friend_ids.append([f for f in friends])

        except Exception as e:
            print(e)
        else:
            f.write(str(friend_ids))



if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('screen_name', type=str)
    args = argparser.parse_args()
    screen_name = args.screen_name
    get_friend_ids(screen_name)