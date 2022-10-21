from time import time


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_execution_time = time()
        result = self.func(*args, **kwargs)
        self.execution_time = time() - start_execution_time
        print(f'Time of execution: {self.execution_time} seconds')
        return result

@Timer
def squares_comprehension(n):
    return [x**2 for x in range(n)]

squares_comprehension(10**6)