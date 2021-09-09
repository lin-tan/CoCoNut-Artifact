from source.training.train import train_lstm

train_lstm(0.5602982715391416, 147, 147, 147, 'True', 8, 4, 0.486489110839442, 0.7457144040641107, 0.799131405959919,
           'nag', 'label_smoothed_cross_entropy',
           './intermediate_repo/lstm/trained/context_tuned_1',
           './intermediate_repo/java/2006/nocontext/train/bin')
