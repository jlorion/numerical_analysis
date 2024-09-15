import argparse
import math
import sympy as smp


def toMathFunc(expression):
    def function(x):
        return round(eval(expression), 7) 
    return function


def bisectionMethod(expression, interval, absoluteError: float):
    kplusone = (interval[0] + interval[1])/2
    while(True):
        runFunction = expression(kplusone)
        print(str(interval[0])+ " |"+ str(interval[1])+ " |" + f"{kplusone:.10f}" + " |"+ f"{runFunction:.10f}")
        if runFunction < 0:
            interval[1] = kplusone
        else:
            interval[0] = kplusone
        if (abs(expression(kplusone)) > absoluteError):
            kplusone = (interval[0] + interval[1])/2
            continue
        else:
            print("x = " + f"{kplusone:.10f}")
            break

def newtonsMeth(expression, initialValue, cap):

    pass

if __name__ == "__main__":
    mathFunc = "(4*x**3) - (12.3*x**2)-x+16.2"
    bisectionMethod(toMathFunc(mathFunc), [1, 2], 0.01)
    
    

    pass
