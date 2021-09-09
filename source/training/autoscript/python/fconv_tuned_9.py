from source.training.train import train_fconv

train_fconv(0.005533347144345613, True, 165, 165, 165, '[(128,6)] * 8', '[(128,8)] * 7', 0.47614411822815284,
            0.6448042062136476, 0.7076638230384297, 'sgd', 'cross_entropy',
            './intermediate_repo/python/nocontext/trained/fconv_tuned_9',
            './intermediate_repo/python/nocontext/train/bin')
