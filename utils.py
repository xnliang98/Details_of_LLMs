import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        end_time = time.time()
        print("函数的运行时间(s)：{}".format(end_time - start_time))
        print("函数的运行时间(ms)：{}".format(float(end_time - start_time) * 1000.0))
        return result
    return wrapper