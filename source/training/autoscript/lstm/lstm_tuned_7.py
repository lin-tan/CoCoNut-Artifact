from source.training.train import train_lstm

train_lstm(0.041642481576288914, 258, 258, 258, 'True', 12, 4, 0.6566183651681773, 0.12301968915576855,
           0.6233770285382559, 'sgd', 'cross_entropy',
           './intermediate_repo/lstm/trained/context_tuned_7',
           './intermediate_repo/java/2006/nocontext/train/bin')
