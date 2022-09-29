from cache_to_disk import cache_to_disk
from time import sleep

@cache_to_disk(10)
def add(a, b):
    print("sleeping")
    sleep(3)
    return a+b


print(add(1, 2))
