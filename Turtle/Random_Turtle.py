from turtle import *
from random import *
import time
import math
a = 0

for i in range(5):
    pendown()
    a= a+2
    for i in range(6):
        forward(a)
        right(60)
    penup()
    left(90)
    forward(2)
    right(90)
    forward(-1)


time.sleep(5)



