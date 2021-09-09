from source.training.train import train_context

train_context(0.2602310837779551, True, 226, 226, 226, '[(512,7)] * 10', '[(640,8)] * 6', 0.15331494861223294,
              0.8794987236596069, 0.6588269008591344, 'nag', 'label_smoothed_cross_entropy',
              './intermediate_repo_good/js/context/trained/context_tuned_7',
              './intermediate_repo_good/js/context/train/bin')
