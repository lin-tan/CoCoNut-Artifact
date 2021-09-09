from source.training.train import train_context

train_context(0.03306673139818872, True, 145, 145, 145, '[(384,7)] * 5', '[(256,10)] * 4', 0.02928000941475195,
              0.1619284190760819, 0.8874468307300051, 'adagrad', 'cross_entropy',
              './intermediate_repo_good/c/context/trained/context_tuned_6',
              './intermediate_repo_good/c/context/train/bin')
