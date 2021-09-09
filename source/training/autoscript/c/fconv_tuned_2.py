from source.training.train import train_fconv

train_fconv(0.0015150814800350965, True, 364, 364, 364, '[(384,3)] * 9', '[(640,4)] * 5', 0.9707029949760514,
            0.8757399970334439, 0.4303474425107823, 'sgd', 'label_smoothed_cross_entropy',
            './intermediate_repo/c/nocontext/trained/fconv_tuned_2',
            './intermediate_repo/c/nocontext/train/bin')
