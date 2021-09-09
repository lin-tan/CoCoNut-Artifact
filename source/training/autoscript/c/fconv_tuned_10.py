from source.training.train import train_fconv

train_fconv(0.07968555756083184, False, 298, 298, 150, '[(512,3)] * 7', '[(640,5)] * 4', 0.6761639971947639,
            0.8913040572948645, 0.7197491571968713, 'sgd', 'cross_entropy',
            './intermediate_repo/c/nocontext/trained/fconv_tuned_10',
            './intermediate_repo/c/nocontext/train/bin')
