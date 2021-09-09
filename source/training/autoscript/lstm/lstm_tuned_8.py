from source.training.train import train_lstm

train_lstm(0.1794366556198035, 418, 418, 359, 'False', 13, 8, 0.8431173609585605, 0.7836281236195715,
           0.6038732725348257, 'nag', 'label_smoothed_cross_entropy',
           './intermediate_repo/lstm/trained/context_tuned_8',
           './intermediate_repo/java/2006/nocontext/train/bin')
