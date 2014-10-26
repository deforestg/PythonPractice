class Fibgen(object):

    memo = [1, 1]
    use_memo = 0

    @staticmethod
    def fib(use_memo=0):
        Fibgen.use_memo = use_memo
        x = 0
        while 1:
            yield Fibgen.fibber(x)
            x += 1

    @staticmethod
    def fibber(x):
        if Fibgen.use_memo and len(Fibgen.memo) > x:
            return Fibgen.memo[x]
        if x < 2:
            return 1

        new = Fibgen.fibber(x - 1) + Fibgen.fibber(x - 2)

        if len(Fibgen.memo) <= x:
            Fibgen.memo.append(new)

        return new