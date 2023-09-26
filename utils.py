import time
import json
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        end_time = time.time()
        print("函数的运行时间(s)：{}".format(end_time - start_time))
        # print("函数的运行时间(ms)：{}".format(float(end_time - start_time) * 1000.0))
        return result
    return wrapper

@time_it
def read_json_lines(file_name):
    with open(file_name, 'r') as file:
        data = [json.loads(line) for line in file]
    return data

@time_it
def save_json_lines(data, file_name):
    with open(file_name, 'w') as file:
        for item in data:
            json.dump(item, file)
            file.write('\n')