import sys


def enter(letter):
    while True:
        try:
            return float(input(f"Please, enter {letter}: "))
        except:
            print("Wrong! Try again!")


def enter_coefficients():
    if len(sys.argv) > 1:
        a = float(sys.argv[1])
        if len(sys.argv) > 2:
            b = float(sys.argv[2])
        else:
            b = enter("B")
        if len(sys.argv) > 3:
            c = float(sys.argv[3])
        else:
            c = enter("C")
    else:
        a = enter("A")
        b = enter("B")
        c = enter("C")
    return a, b, c


def calculate(a, b, c):
    d = b ** 2 - 4 * a * c
    solution = []
    if d == 0:
        r = -b / (2 * a)
        solution.append(r)
    elif d > 0:
        r1 = (-b - d ** 0.5) / (2 * a)
        r2 = (-b + d ** 0.5) / (2 * a)
        solution.append(r1)
        solution.append(r2)
    return solution


def output(a, b, c, solution):
    print(f"A: {a}; B: {b}; C: {c}. ")
    if len(solution) == 0:
        print("No roots :( ")
    elif len(solution) == 1:
        print(f"One root: {solution[0]} :)")
    else:
        print(f"Two roots: {solution[0]} and {solution[1]} ^U^")


def main():
    a, b, c = enter_coefficients()
    solution = calculate(a, b, c)
    output(a, b, c, solution)


if __name__ == "__main__":
    main()
