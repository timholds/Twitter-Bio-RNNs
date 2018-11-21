from __future__ import print_function
import twitter
import requests
import time
from passwords import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


# Get the user's friend's IDs of
def get_friend_ids(screen_name):
    friend_ids = []

    with open('friendIDs.txt', 'w') as f:
        try:
            friends = api.GetFriendIDs(screen_name)
            friend_ids.append([f for f in friends])

        except Exception as e:
            print(e)
        else:
            f.write(str(friend_ids))


# Get the user ID's of the friends of friends
def get_fof_ids(friends_ids_file):

    # Read all the ids from the FriendIDs.txt and append each of their friends' IDS to the list ids
    with open(friends_ids_file, 'r') as file:

        for line in file:
            friend_ids = line.split(',')

            with open('fofIDs.txt', 'w') as f:
                for friend_id in friend_ids:
                    print('getting friends of friends for friend with id #{}'.format(friend_id))
                    ids = []
                    try:
                        fof_ids = api.GetFriendIDs(user_id=friend_id, total_count=2000)
                        ids.append([user_id for user_id in fof_ids])
                        time.sleep(60)

                    except Exception as e:
                        print(e)
                        time.sleep(60)

                    else:
                        f.write(str(ids))


# Get the biographies of the friends of friends
def get_bios(all_ids_file):

    with open(all_ids_file, 'r') as file:
        for line in file:
            fof_ids = line.split(',')

            with open('biographies.txt', 'w+') as f:
                for fof_id in fof_ids:
                    print('getting bio for id #{}'.format(fof_id))
                    bio_list = []
                    try:
                        bio = api.GetUser(user_id=fof_id, include_entities=False).description
                    except requests.ConnectionError:
                        print("No Internet")
                    else:
                        print(bio)
                        bio_list.append(bio)
                        time.sleep(1)
                        f.write(bio_list)

def main(username):
    get_friend_ids(username)
    get_fof_ids('friendIDs.txt')
    get_bios('fofIds.txt')


main('timholds')