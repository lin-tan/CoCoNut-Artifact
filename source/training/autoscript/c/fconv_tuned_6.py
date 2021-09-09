from source.training.train import train_fconv

train_fconv(0.01746815092960441, True, 205, 205, 205, '[(640,5)] * 10', '[(256,5)] * 3', 0.54895795284263,
            0.5612220821359721, 0.5178729791525679, 'sgd', 'label_smoothed_cross_entropy',
            './intermediate_repo/c/nocontext/trained/fconv_tuned_6',
            './intermediate_repo/c/nocontext/train/bin')
