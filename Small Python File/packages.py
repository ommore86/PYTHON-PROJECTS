import mypkg.p1, mypkg.p2
mypkg.p1.m1()
mypkg.p2.m2()

from mypkg.p1 import m1
m1()

from mypkg.p1 import m1 as func
func()

from mypkg import p1, p2
p1.m1()
p2.m2()