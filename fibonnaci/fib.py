def fib(x):
    def _fib_inner(start, result, index):
        if index == x:
            return result
        return _fib_inner(result, start + result, index + 1)

    return _fib_inner(0, 1, 0)
