from typing import Callable

def counter_decorator(f: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        n = wrapper.count
        print("Function calls count:",n)
        return f(*args, **kwargs)
    
    wrapper.count = 0
    return wrapper

def projection_decorator(f: Callable[[int], None]) -> Callable[[int, int, int], None]:
    def calcu(x, y ,z):
        result = 3*x -7*y+15*z+18
        return f(result)
    return calcu
def sum(a: int, b: int):

    print(a + b)



fn = counter_decorator(sum)

fn(1, 2)

fn(4, 5)

fn(-4, 5)

