from typing import Tuple, List, Dict # Beware the file name! The name of this file was "types" and there was a library named that which fucked up the import
# Only imports what you need, if you know what you need
from enum import Enum

def my_func(a):
    print(a)
    pass

my_func("hej")


def my_func2(a:tuple): # Defines the variable as a tuple
    print(a)
    pass

my_func2("hej")

def my_func(a:tuple[int, str, bool], b:list[int]): # By using the imported types, we can define what types each input should have
    print(a, b)
    pass

my_func((1, 'hej', True), [1,2,3]) # hovering over my_func, you can see what types should be entered.
# But this seems to work anyway, what's the point?

