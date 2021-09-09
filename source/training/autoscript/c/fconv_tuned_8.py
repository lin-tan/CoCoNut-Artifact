from source.training.train import train_fconv

train_fconv(0.11623805689340105, True, 106, 106, 106, '[(128,6)] * 3', '[(128,3)] * 6', 0.3782428365044066,
            0.12996300945594275, 0.7808700149034068, 'adagrad', 'label_smoothed_cross_entropy',
            './intermediate_repo/c/nocontext/trained/fconv_tuned_8',
            './intermediate_repo/c/nocontext/train/bin')
