from source.training.train import train_trans

train_trans(0.2093217889131065, 0.0763446704385462, 0.0012709497771422607, 30, 30, 10, 10, 2, 13, 0.22930923862160757,
            0.517785770779982, 0.6551429487055231, 'sgd', 'cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_2',
            './intermediate_repo/java/2006/nocontext/train/bin')
