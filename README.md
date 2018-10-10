#AutoBio

In this project, we generate Twitter Biographies using RNNs(Recurrent Neural Nets).
Given any user ID, the code finds all of their friends, and the friends of all of their friends,
then collects the bios of up to 10,000 of these users. We then use a RNN to learn the conditional
probabilities between letters. Lastly, we use this RNN to generate new biographies that are 140 characters each.


# TODO limit the number of IDs in friends of friends

### Installing

Download the code: `pip install -r requirements.txt`
Run the tests for the python-twitter package `***TEST CODE`


### Getting started with Twitter API

Set up an Twitter developer account.
Afterwards, or if you already have a developer account, create a new app.
Get the account and project authorizations and put them into a new file passwords.py like so:

TWITTER_CONSUMER_KEY_PASS = 'STRING'
TWITTER_CONSUMER_SECRET_PASS = 'STRING'
TWITTER_ACCESS_TOKEN_KEY_PASS = 'STRING'
TWITTER_ACCESS_TOKEN_SECRET_PASS = 'STRING'

**To Find your Twitter ID**:
1) Go to www.twitter.com and sign in
2) Click your profile at the top right and go to `Settings and Privacy`
3) Click on `Your Twitter Data`
4) Enter your password and hit confirm
5) See the USER ID

Pick two characters that you want the sentences to start with.
We created examples when the first two letters are "Th" and "I "


### Using

## Dataset

TODO make sure it prints the right file names and that the next file can read it with this name

1) Get your friends IDs by passing in your ID to `get_friends.py`, which creates a file called `FriendIDs.txt`
```
> python get_friends.py 01221414
```

2) Get your friends of friends' IDs by calling `get_fof.py` and passing it `FriendIDs.txt`, which creates a file get `FoFIDs.txt`
```
> python get_fof.py FriendIDs.txt
```

3) Get all user biographies by calling `get_bios.py` and passing in `FoFIDs.txt`, which creates a file called `Bios.txt`
```
> python get_bios.py FoFIDs.txt
```


## Training and Generating
4) Train
Train a RNN on all the biographies by calling `train.py` and passing it `Bios.txt`

```
> python train.py Bios.txt

Training for 2000 epochs...
(10 minutes later)
Saved as Bios.pt
```

5) Generate
After training the model will be saved as [filename].pt
Now run `generate_bios.py` with that filename to generate some new bios.
Also pass in two letters that each bio should start with. I recommend `Th` to start. You might want to think of other common
beginnings to bios/sentences in general and pass in these two letters.

```
> python generate_bios.py Bios.pt --prime_str "Th"
```

Training options
```
Usage: train.py [filename] [options]

Options:
--n_epochs         Number of epochs to train
--print_every      Log learning rate at this interval
--hidden_size      Hidden size of GRU
--n_layers         Number of GRU layers
--learning_rate    Learning rate
--chunk_len        Length of chunks to train on at a time
```

Generation options
```
Usage: generate.py [filename] [options]

Options:
-p, --prime_str      String to prime generation with
-l, --predict_len    Length of prediction
-t, --temperature    Temperature (higher is more chaotic)
```

7) (Optional) Call temp-iterator.py and pass in a value between 0 and 1 to test out the algorithm at different temperatures. Higher temperatures
make the output more unpredictable, while lower temperatures make them more regular

TODO find actual examples
```
Example sentence with too low of a temp
Example sentence with too high of a temp


End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system


## Authors

* **Tim Holdsworth** - *Initial work* - [PurpleBooth](https://github.com/timholds/AutoBio)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Used code and text from the tutorial here: https://github.com/spro/practical-pytorch/tree/master/char-rnn-generation
