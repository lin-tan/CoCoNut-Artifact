from source.training.train import train_lstm

train_lstm(0.37924863524741836, 450, 450, 311, 'False', 15, 2, 0.5960035855098742, 0.3631337588636806,
           0.23276525124097602, 'sgd', 'cross_entropy',
           './intermediate_repo/lstm/trained/context_tuned_9',
           './intermediate_repo/java/2006/nocontext/train/bin')
