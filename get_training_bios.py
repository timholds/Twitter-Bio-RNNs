#!/usr/bin/env python

# Copyright 2016 The Python-Twitter Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ------------------------------------------------------------------------
# Change History
# 2010-10-01
#   Initial commit by @jsteiner207
#
# 2014-12-29
#   PEP8 update by @radzhome
#
# 2016-05-07
#   Update for Python3 by @jeremylow
#

from __future__ import print_function
import twitter
import requests
from passwords import TWITTER_CONSUMER_KEY_PASS, TWITTER_CONSUMER_SECRET_PASS, TWITTER_ACCESS_TOKEN_KEY_PASS, TWITTER_ACCESS_TOKEN_SECRET_PASS
import time


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


def get_friend_ids():
    user_ids = []

    with open('friend_ids.txt', 'w') as f:
        try:
            users = api.GetFriendIDs()
            user_ids.append([u for u in users])
            #print([u.user_id for u in users])

        except Exception as e:
            print(e)
        else:
            #pass
            f.write(str(user_ids))

    return user_ids

def get_fof_ids(friend_ids):
    ids = []

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

    return ids

def get_bios(ids):
    bio_list = []
    with open('bios.txt', 'wb') as f:

        for id in ids:
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
'''


friend_ids = get_friend_ids()
#print(type(friend_ids))
get_fof_ids(friend_ids)
#all_ids = pd.read_csv()
#get_bios(all_ids)