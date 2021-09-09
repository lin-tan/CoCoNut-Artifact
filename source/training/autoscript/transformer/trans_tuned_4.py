from source.training.train import train_trans

train_trans(0.3981184261521661, 0.15471289019986323, 0.7811925284063347, 51, 51, 17, 17, 1, 1, 0.3746747170012018,
            0.5143058134538046, 0.8797562752520806, 'nag', 'label_smoothed_cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_4',
            './intermediate_repo/java/2006/nocontext/train/bin')
