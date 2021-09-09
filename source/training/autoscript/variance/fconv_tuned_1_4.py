from source.training.train import train_fconv

train_fconv(0.14750324647058333, True, 353, 353, 353, '[(384,6)] * 8', '[(512,10)] * 5', 0.7915283934586732,
            0.5498989114182679, 0.3526243918050602, 'nag', 'cross_entropy',
            '/home/mydir/issta_data/final/fairseq-data/2006/nocontext/trained/fconv_tuned_1.4',
            './intermediate_repo/java/2006/nocontext/train/bin')
