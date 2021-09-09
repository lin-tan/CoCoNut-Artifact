from source.training.train import train_context

train_context(0.03421960641764166, False, 116, 116, 360, '[(128,4)] * 9', '[(640,10)] * 8', 0.286739379371575,
              0.8469909165285214, 0.7517948821073919, 'nag', 'label_smoothed_cross_entropy',
              './intermediate_repo_good/js/context/trained/context_tuned_1',
              './intermediate_repo_good/js/context/train/bin')
