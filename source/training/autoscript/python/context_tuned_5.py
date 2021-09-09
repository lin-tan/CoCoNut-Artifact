from source.training.train import train_context

train_context(0.0059120677320028125, False, 326, 326, 242, '[(512,5)] * 10', '[(640,2)] * 6', 0.9846969173516326,
              0.639484543640567, 0.2927570878644937, 'sgd', 'label_smoothed_cross_entropy',
              './intermediate_repo_good/python/context/trained/context_tuned_5',
              './intermediate_repo_good/python/context/train/bin')
