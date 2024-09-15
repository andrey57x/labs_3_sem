import sys

def enter(letter):
    while True:
        try:
            return float(input(f"Please, enter {letter}: "))
        except:
            print("Wrong! Try again!")

class Equation:
    def __init__(self):
        self.a, self.b, self.c, self.solution = 0, 0, 0, []

    def enter_coefficients(self):
        if len(sys.argv) > 1:
            self.a = float(sys.argv[1])
            if len(sys.argv) > 2:
                self.b = float(sys.argv[2])
            else:
                self.b = enter("B")
            if len(sys.argv) > 3:
                self.c = float(sys.argv[3])
            else:
                self.c = enter("C")
        else:
            self.a = enter("A")
            self.b = enter("B")
            self.c = enter("C")

    def calculate(self):
        d = self.b ** 2 - 4 * self.a * self.c
        if d == 0:
            r = -self.b / (2 * self.a)
            self.solution.append(r)
        elif d > 0:
            r1 = (-self.b - d ** 0.5) / (2 * self.a)
            r2 = (-self.b + d ** 0.5) / (2 * self.a)
            self.solution.append(r1)
            self.solution.append(r2)


    def print(self):
        print(f"A: {self.a}; B: {self.b}; C: {self.c}. ")
        if len(self.solution) == 0:
            print("No roots :( ")
        elif len(self.solution) == 1:
            print(f"One root: {self.solution[0]} :)")
        else:
            print(f"Two roots: {self.solution[0]} and {self.solution[1]} ^U^")


    def solve(self):
        self.enter_coefficients()
        self.calculate()
        self.print()



if __name__ == "__main__":
    eq = Equation()
    eq.solve()
