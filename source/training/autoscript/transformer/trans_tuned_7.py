from source.training.train import train_trans

train_trans(0.32253445224141, 0.17869680927482934, 0.4216883794980034, 30, 30, 5, 5, 10, 11, 0.0444016440631948,
            0.7336597502906265, 0.7722013981026856, 'sgd', 'label_smoothed_cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_7',
            './intermediate_repo/java/2006/nocontext/train/bin')
