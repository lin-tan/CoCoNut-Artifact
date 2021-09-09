from source.training.train import train_lstm

train_lstm(0.9598137732207281, 492, 492, 492, 'False', 20, 1, 0.02050127498582832, 0.03128046100000481,
           0.7170075758395127, 'adagrad', 'cross_entropy',
           './intermediate_repo/lstm/trained/context_tuned_2',
           './intermediate_repo/java/2006/nocontext/train/bin')
