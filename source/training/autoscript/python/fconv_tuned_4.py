from source.training.train import train_fconv

train_fconv(0.19373178358250154, False, 79, 79, 421, '[(128,7)] * 5', '[(384,7)] * 2', 0.0826909790618301,
            0.9715605504864337, 0.8740403099836496, 'adagrad', 'label_smoothed_cross_entropy',
            './intermediate_repo/python/nocontext/trained/fconv_tuned_4',
            './intermediate_repo/python/nocontext/train/bin')
