from typing import Callable

def outer() -> tuple[Callable[[], None], Callable[[int], None]]:
    t = 2

    def modify_t(new_t: int) -> None:
        #declare t to be reference of outer t 
        nonlocal t
        t = new_t
    
    def print_t() -> None:
        print(t)

    return modify_t, print_t


func_mod, func_print = outer()

func_print()
func_mod(8)
func_print()

func_mod2, func_print2 = outer()

func_print2()
