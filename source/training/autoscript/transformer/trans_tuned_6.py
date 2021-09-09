from source.training.train import train_trans

train_trans(0.6233368334410994, 0.3320490579099852, 0.4715466753714732, 64, 64, 8, 8, 8, 5, 0.8277178619958471,
            0.4640292213713664, 0.3955451985810887, 'nag', 'label_smoothed_cross_entropy',
            './intermediate_repo/transformer/trained/context_tuned_6',
            './intermediate_repo/java/2006/nocontext/train/bin')
