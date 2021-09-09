from source.training.train import train_context

train_context(0.06179165410667997, True, 107, 107, 107, '[(384,3)] * 2', '[(640,7)] * 7', 0.5923928699341593,
              0.6517291271041699, 0.3515853139423949, 'nag', 'cross_entropy',
              './intermediate_repo_good/js/context/trained/context_tuned_3',
              './intermediate_repo_good/js/context/train/bin')
