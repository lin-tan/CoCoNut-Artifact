from source.training.train import train_lstm

train_lstm(0.31771828103827204, 464, 464, 217, 'False', 6, 5, 0.09671598011844706, 0.9477805303415001,
           0.28632740175003457, 'nag', 'label_smoothed_cross_entropy',
           './intermediate_repo/lstm/trained/context_tuned_6',
           './intermediate_repo/java/2006/nocontext/train/bin')
