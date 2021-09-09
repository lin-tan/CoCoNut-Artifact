from source.training.train import train_trans

train_trans(0.1405272815259654, 0.8518603923074012, 0.612071653110651, 42, 42, 14, 14, 11, 4, 0.590730091880669,
            0.7493490123278396, 0.7679617328918502, 'sgd', 'label_smoothed_cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_9',
            './intermediate_repo/java/2006/nocontext/train/bin')
