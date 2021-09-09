from source.training.train import train_fconv

train_fconv(0.2725394635166619, False, 177, 177, 133, '[(128,4)] * 9', '[(512,8)] * 9', 0.9918597645185625,
            0.78117645727482, 0.7679435945955843, 'nag', 'cross_entropy',
            './intermediate_repo/java/2006/nocontext/trained/fconv_tuned_7',
            './intermediate_repo/java/2006/nocontext/train/bin')
