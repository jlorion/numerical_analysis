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
    parser = argparse.ArgumentParser(description="Numerical Analysis Programming cuz dis shit be programmablbe \n \n Ex. python NumA.py -b (2*x**2)-(4*x)-2 -e 0.05 -i [0, 5]")

    parser.add_argument('-b', '--bisection', help="for bisection method function after the flag ")
    parser.add_argument('-i', '--interval', help="define the interval default is [5,5]")
    parser.add_argument('-e', '--error', help='defines the absolute error for function termination default is 0.05')

    defaultInterval = [0, 5]
    defaultError = 0.05

    args = parser.parse_args()

    funx = toMathFunc(args.bisection) if args.bisection is not None else toMathFunc("(2*x**2)-(4*x)-2")
    interval = eval(args.interval) if args.interval is not None else defaultInterval
    errorx = eval(args.error) if args.error is not None else defaultError
    bisectionMethod(funx, interval, errorx)
    

    pass
