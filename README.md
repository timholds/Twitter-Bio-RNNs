  # AutoBio
  
  ## Overview
  In this project, we collect Twitter biographies using the Twitter API and generate original bios using a character level RNN (recurrent neural net).
  
  Given any username, the code finds all of their friends, and the friends of all of their friends, then collects the bios of up to 10,000 of these users. We then train the RNN on these bios and use the model to generate new biographies that are 140 characters each.
  
  
  ## Python Scripts
  ### Dataset
  You can either train a RNN using the same dataset that I collected from my friends, called bios-example.txt, or collect your own bios.
  
  To generate your own dataset based on the bios of your friends, first set up a Twitter developer account. Afterwards, or if you already have a developer account, create a new app. Get the account and project authorizations and put them into a new file passwords.py like so, replacing 'STRING' with the actual value given to you by Twitter:
  
  TWITTER_CONSUMER_KEY_PASS = 'STRING'  
  TWITTER_CONSUMER_SECRET_PASS = 'STRING'  
  TWITTER_ACCESS_TOKEN_KEY_PASS = 'STRING'  
  TWITTER_ACCESS_TOKEN_SECRET_PASS = 'STRING'  
  
  You will then need to run main function on the `get_training_bios.py` script with your Twitter username instead of mine (see line 83 to make the change). This should create 3 files - `friendIDs.txt`, `fofIDs.txt`, and `bios.txt`.
  
  `bios.txt` contains all the data we will train our RNN on.
  
  For example, here is snippet from all the bios we collected:
  
  ```
  Director of Communications for NEO Philanthropy and director of Strategic Communications Initiative for Four Freedoms Fund (FFF), a fund of NEO.
  #Research and news in #ConsumerBehavior and #MarketingScience from the @NYUStern #Marketing Department.
  IaaS, Open Source & @nodejs Architect at @Oath (formerly @yahoo). I created @HackSI & @HackSI_Lights, I mentor @MARS_Robotics & I ❤️ Drones.
  T. Rowe Price delivers investment insights to keep you informed and help your clients make better investment decisions.
  Precision Business Insights, is a global market research and business consulting firm, caters to the Healthcare, Agriculture, and F&B, and ICT Industry.
  UC Berkeley's official startup accelerator. We help Cal entrepreneurs and transformational startups. Bring us your moonshot!
  animator of weird stuff.
  Popping up all over the place. We are funguys of digital marketing helping our clients rapidly expand and grow online. DM for business enqs.
  director of technology at @givewithus, (part of @ecomediacbs) and drummer. past engineer at @warbyparker, @HODINKEE, @sherpaahealth, @manahealth.
  ```
  
  
  ### Training and Generating
  Train a RNN on all the biographies by calling `train.py` and passing it the `biographies.txt` that you generated in the first part or pass `bios-example.txt` to use the bios I have collected
  
  ```
  > python train.py biographies.txt
  
  Training for 2000 epochs...
  (10 minutes later)
  Saved as Bios.pt
  ```
  
  Generate
  After training the model will be saved as [filename].pt  
  Now run `generate.py` with that filename to generate some new bios.Pass in two letters that each bio should start with. I recommend `Th` to start. You might want to think of other common beginnings to bios/sentences in general and pass in these two letters.
  
  ```
  > python generate_bios.py Bios.pt --prime_str "Th"
  ```
  
  Here is a snippet of the results:
  ```
  Thing the supports and on the world biter of Conner of designer, engineer of the starting and the https://t.co/233w9ur9494kdt. Professions & b
  Therian, Iffing and startupports and source bent reprent of the products. I starting and soment on commant of the medial student of the Produc
  The & Products. Spine with and denery of the Infounder of the mounder startics and where the web like mare strater, startuper & startupplower
  Th @IBL
  Harker, Berk Engineer, Science & Lead art https://t.co/9l4A3KKZfff
  Thing of on community and mart of the startups and in beantan & student productor, starting startive on the this of the studer of the research
  The Scienting and social liver, startuper, experent and in computer denering and the products & startist art research and dad science startupi
  ```
  
  Changing the temperature to be lower gives more predictable results, but often repeats words. It seems like this method needs more training data and perhaps a longer priming string to produce intelligible results. Since this was a practice project to get comfortable with RNNs, I have not invested the time to play with the hyper-parameters. In the future one thing I would like to do is to train models at different temperatures and compare their results.
  
  Interestingly enough, the model learns how Twitter links work, that many people I follow work have the words startup, science, design, engineering, and art in their bios. I'd like to see how this model performs on other Twitter users who use Twitter differently. 
  
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
  
  ## Authors
  
  * **Tim Holdsworth**  [AutoBio](https://github.com/timholds/AutoBio)
  * Used code from **this tutorial**: https://github.com/spro/practical-pytorch/tree/master/char-rnn-generation
  
  
  ## License
  
  This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
  
  ## Acknowledgments
  
  * Used code and text from the tutorial here: https://github.com/spro/practical-pytorch/tree/master/char-rnn-generation
  
  ### TODO
  Limit the number of IDs in friends of friends

