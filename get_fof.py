from __future__ import print_function
import twitter
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


# TODO make sure this actually works with the .txt file format
def get_fof_ids(friends_ids_file):
    all_ids = []

    # Read all the ids from the FriendIDs.txt and append each of their friends' IDS to the list ids
    with open(friends_ids_file, 'r') as file:

        for line in file:
            friend_ids = line.split(',')

            with open('FoFIDs.txt', 'w') as f:
                for id in friend_ids:
                    try:
                        print('getting friends of friends for friend id {}'.format(id))
                        fof_ids = api.GetFriendIDs(user_id=id, total_count=2000)
                        all_ids.append([fof_id for fof_id in fof_ids])
                        time.sleep(60)

                    except Exception as e:
                        print(e)
                        time.sleep(60)

                    else:
                        f.write(str(all_ids))


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('FriendIDs', type=str)
    args = argparser.parse_args()
    friend_ids = args.FriendIDs
    get_fof_ids(friend_ids)

'''
def get_fof_ids_old():
    with open('all_ids.txt', 'w') as f:
        # For each our your friends, get all of their friends
        for list in friend_ids:
            for id in list:
                try:
                    #friends_of_friends = api.getFriends(user_id=id, skip_status=True, total_count=2000)
                    print('getting friends of friends for friend id {}'.format(id))
                    fof = api.GetFriendIDs(user_id=id, total_count=2000)
                    ids.append([friend_id for friend_id in fof])
                    time.sleep(60)

                except Exception as e:
                    print(e)
                    time.sleep(60)

                else:
                    f.write(str(ids))

    #return ids
    '''
