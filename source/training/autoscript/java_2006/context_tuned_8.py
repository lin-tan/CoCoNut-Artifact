from source.training.train import train_context

train_context(0.08225774673913022, True, 185, 185, 185, '[(384,8)] * 2', '[(256,9)] * 10', 0.43749747624711577,
              0.41291139635553753, 0.6345506727991334, 'sgd', 'cross_entropy',
              './intermediate_repo_good/java/2006/context/trained/context_tuned_8',
              './intermediate_repo_good/java/2006/context/train/bin')
