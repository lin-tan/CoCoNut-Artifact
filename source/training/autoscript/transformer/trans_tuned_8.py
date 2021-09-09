from source.training.train import train_trans

train_trans(0.050994038531622654, 0.3093358562652223, 0.2809754812394243, 30, 30, 6, 6, 16, 4, 0.10245019529285959,
            0.036244652119179266, 0.857292590342015, 'sgd', 'cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_8',
            './intermediate_repo/java/2006/nocontext/train/bin')
