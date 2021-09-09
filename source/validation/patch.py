class Patch(object):
    source = ""
    target = ""
    patch = ""
    id = ""
    model = ""
    context = ""
    row_num = 0
    score = 0.0
    meta = ""
    rank = 0

    def __init__(self, source, target, patch, id, row_num, score, meta, model, context, rank):
        self.source = source
        self.target = target
        self.patch = patch
        self.id = id
        self.row_num = row_num
        self.score = score
        self.meta = meta
        self.model = model
        self.context = context
        self.rank = rank