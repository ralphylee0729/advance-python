from typing import Callable, Any

def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
    print("wraaping")
    def inner(*args:Any, **kwargs: Any) -> Any:
        print("execute wrapping")
        result=fn(*args, **kwargs)
        return result
    
    return inner


@wrapper
def do_it(a: int, b: int) -> int:
    return a + b

#wrapped_do_it = wrapper(do_it)
#print(wrapped_do_it(1,2))
#f1 = do_it
#print(f1(1,2))
print(do_it(1,2))