import func
func.stud("Om",8)

from func import stud
stud("Om", 10)

from func import square, hello
print(square(3))
print(hello("Ok"))

from func import *
stud("Om", 10)
print(square(3))
print(hello("Ok"))

import func as f
f.stud("Om",2)