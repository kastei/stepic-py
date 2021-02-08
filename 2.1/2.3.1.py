class MultiFilter:

    def judge_half(self, pos, neg):
        return pos >= neg

    def judge_any(self, pos, neg):
        return pos > 0

    def judge_all(self, pos, neg):
        return neg == 0

    def pos(self, x, funcs):
        res = 0
        for f in funcs:
            if f(x):
                res += 1
        return res

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.funcs = funcs
        self.judge = judge
        self.iterable = iterable

    def __next__(self):
        x = self.iterable.next()
        pos = pos(x, self.funcs)
        neg = len(self.funcs) - pos
        if self.judge(pos, neg):
            return x
        else:
            return self.next()

    def __iter__(self):
        return iter(self.iterable)
