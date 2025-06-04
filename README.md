# AutoBio

In this project, we generate Twitter Biographies using RNNs(Recurrent Neural Nets). Given any user ID, the code finds all of their friends, and the friends of all of their friends,then collects the bios of up to 10,000 of these users. We then use a RNN to learn the conditional
probabilities between letters. Lastly, we use this RNN to generate new biographies that are 140 characters each.

### To generate Twitter bios using your friends' bios

Download the code from [github](https://github.com/timholds/Twitter-Bio-RNNs) and install the requirements: `pip install -r requirements.txt` 

### Getting started with Twitter API

Set up an Twitter developer account and create a new app.  

**To Find your Twitter ID**:
1) Go to www.twitter.com and click your profile at the top right and go to `Settings and Privacy`  
2) Click on `Your Twitter Data`  
3) Enter your password and hit confirm to see the USER ID 

## Dataset

1) Find your Twitter ID

2) Get your friends IDs by passing in your ID to `get_friends.py`, which creates a file called `FriendIDs.txt`
```
> python get_friends.py 01221414
```

3) Get your friends of friends' IDs by calling `get_fof.py` and passing it `FriendIDs.txt`, which creates a file get `FoFIDs.txt`
```
> python get_fof.py FriendIDs.txt
```

4) Get all user biographies by calling `get_bios.py` and passing in `FoFIDs.txt`, which creates a file called `Bios.txt`
```
> python get_bios.py FoFIDs.txt
```


## Training and Generating
5) Train 
Train a RNN on all the biographies by calling `train.py` and passing it `Bios.txt`

```
> python train.py Bios.txt

Training for 2000 epochs...
(10 minutes later)
Saved as Bios.pt
```

6) Generate
After training the model will be saved as [filename].pt 
Now run `generate_bios.py` with that filename to generate some new bios.
Pick two characters that you want the sentences to start with.
We created examples when the first two letters are "Th" and "I "

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


## Challenges
Language Mixing. I had to manually remove the IDs of my friends that follow a lot of people that tweet in different languages, and even so friends of friends still leaked in some non-english tweets.   

Sampling and getting the temperature just right for maximmum comedic effect (and not getting stuck in a "the" loop)  

## Authors

* **Tim Holdsworth** - *Initial work* - [PurpleBooth](https://github.com/timholds/AutoBio)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Used code and text from the tutorial here: https://github.com/spro/practical-pytorch/tree/master/char-rnn-generation
