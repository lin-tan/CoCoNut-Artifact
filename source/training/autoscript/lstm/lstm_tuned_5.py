from source.training.train import train_lstm

train_lstm(0.29896773955160305, 444, 444, 444, 'False', 15, 1, 0.409019825586761, 0.9539643194431885,
           0.6516739877281261, 'sgd', 'label_smoothed_cross_entropy',
           './intermediate_repo/lstm/trained/context_tuned_5',
           './intermediate_repo/java/2006/nocontext/train/bin')
