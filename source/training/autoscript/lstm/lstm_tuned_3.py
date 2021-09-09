from source.training.train import train_lstm

train_lstm(0.42363818894484107, 311, 311, 311, 'True', 3, 1, 0.9618696347386092, 0.849497429877694, 0.9849725571820901,
           'sgd', 'label_smoothed_cross_entropy',
           './intermediate_repo/lstm/trained/context_tuned_3',
           './intermediate_repo/java/2006/nocontext/train/bin')
