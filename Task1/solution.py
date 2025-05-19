def strict(func):
    types = func.__annotations__
    def wrap(*args, **kwargs):
        args_types = [type(arg) for arg in args]
        right_types = [r_arg for r_arg in list(types.values())[:-1]]
        if args_types != right_types:
            raise TypeError("Check the types!!!")
        return func(*args)
    return wrap


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def all_types(g: str, h: int, j:float, p: bool, k: list) -> str:
    return g + str(h) + str(j) + str(p) + str(k)

print(sum_two(1, 2))  # >>> 3
print(all_types('hjhj', 7, 5.66, True, [1, 4, 5]))


