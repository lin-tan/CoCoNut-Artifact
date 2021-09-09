from source.training.train import train_trans

train_trans(0.36757118429123703, 0.2077472553022901, 0.23458028958313615, 16, 16, 2, 2, 2, 1, 0.04523705535400846,
            0.5171673914366653, 0.1705892332229475, 'adagrad', 'label_smoothed_cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_10',
            './intermediate_repo/java/2006/nocontext/train/bin')
