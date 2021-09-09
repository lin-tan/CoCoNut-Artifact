from source.training.train import train_fconv

train_fconv(0.10016184198732148, False, 318, 318, 424, '[(640,6)] * 5', '[(512,4)] * 7', 0.6139086403831485,
            0.7625187615698749, 0.21037956787358847, 'nag', 'cross_entropy',
            './intermediate_repo/java/2006/nocontext/trained/fconv_tuned_3',
            './intermediate_repo/java/2006/nocontext/train/bin')
