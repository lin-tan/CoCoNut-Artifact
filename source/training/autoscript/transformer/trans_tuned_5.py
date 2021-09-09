from source.training.train import train_trans

train_trans(0.019427969980932214, 0.879396402309091, 0.15765509622811735, 49, 49, 7, 7, 19, 6, 0.9248519582981981,
            0.11644451147648227, 0.9347687251801662, 'sgd', 'label_smoothed_cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_5',
            './intermediate_repo/java/2006/nocontext/train/bin')
