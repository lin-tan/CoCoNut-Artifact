from source.training.train import train_fconv

train_fconv(0.14750324647058333, True, 353, 353, 353, '[(384,6)] * 8', '[(512,10)] * 5', 0.7915283934586732,
            0.5498989114182679, 0.3526243918050602, 'nag', 'cross_entropy',
            './intermediate_repo/js/nocontext/trained/fconv_tuned_1',
            './intermediate_repo//js/nocontext/train/bin')
