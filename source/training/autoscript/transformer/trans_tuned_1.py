from source.training.train import train_trans

train_trans(0.2575859519918646, 0.1494679023482045, 0.5554824467095308, 56, 56, 7, 7, 1, 5, 0.8746485384317254,
            0.6734637720083273, 0.6217409511040646, 'nag', 'label_smoothed_cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_1',
            './intermediate_repo/java/2006/nocontext/train/bin')
