import torch
import time
import random
import torch.nn as nn
from torch.autograd import Variable
from NN import evaluate, train, n_characters, random_training_set, time_since, RNN


# A function that runs this whole file with different values of temperature
def runNN_at_diff_temps():
    #for temp in range(0, 1.2, .05):
    for temp in [temp * 0.1 for temp in range(0, 12)]:
        print('temperature parameter is:', temp)
        # Return the predicted string
        evaluate(prime_str='A', predict_len=150, temperature=temp)
        inp, target = random_training_set()
        train(inp, target)

        n_epochs = 2000
        print_every = 120
        plot_every = 10
        hidden_size = 100
        n_layers = 1
        lr = 0.005

        decoder = RNN(n_characters, hidden_size, n_characters, n_layers)
        decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr=lr)
        criterion = nn.CrossEntropyLoss()

        start = time.time()
        all_losses = []
        loss_avg = 0

        for epoch in range(1, n_epochs + 1):
            loss = train(*random_training_set())
            loss_avg += loss

            if epoch % print_every == 0:
                print('[%s (%d %d%%) %.4f]' % (time_since(start), epoch, epoch / n_epochs * 100, loss))
                print(evaluate('Th', 120), '\n')

            if epoch % plot_every == 0:
                all_losses.append(loss_avg / plot_every)
                loss_avg = 0

runNN_at_diff_temps()
