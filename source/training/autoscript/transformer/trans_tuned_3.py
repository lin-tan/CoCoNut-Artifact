from source.training.train import train_trans

train_trans(0.3918836523362682, 0.2866063742988716, 0.8368373405074787, 45, 45, 5, 5, 4, 9, 0.5728066858162262,
            0.36075574621198214, 0.5926695306252778, 'sgd', 'label_smoothed_cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_3',
            './intermediate_repo/java/2006/nocontext/train/bin')
