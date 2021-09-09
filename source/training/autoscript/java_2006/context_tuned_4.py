from source.training.train import train_context

train_context(0.01003413732700531, True, 453, 453, 453, '[(128,7)] * 6', '[(256,5)] * 10', 0.3522433662887732,
              0.8214180717637588, 0.4412316782657021, 'sgd', 'label_smoothed_cross_entropy',
              './intermediate_repo_good/java/2006/context/trained/context_tuned_4',
              './intermediate_repo_good/java/2006/context/train/bin')
