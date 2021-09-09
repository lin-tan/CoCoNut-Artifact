from source.training.train import train_fconv

train_fconv(0.013546188834337558, True, 338, 338, 338, '[(512,3)] * 5', '[(256,2)] * 10', 0.4533926744655141,
            0.8739175382786576, 0.453844146437531, 'nag', 'label_smoothed_cross_entropy',
            './intermediate_repo/java/2010/nocontext/trained/fconv_tuned_5',
            './intermediate_repo/java/2010/nocontext/train/4/bin')
