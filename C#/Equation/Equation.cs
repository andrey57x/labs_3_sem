namespace Equation
{
    internal class Equation
    {
        private double a, b, c;
        private double[] solutions = Array.Empty<double>();
        public Equation(double a = 0, double b = 0, double c = 0)
        {
            this.a = a;
            this.b = b;
            this.c = c;
        }
        public void SetCoefs(double a = 0, double b = 0, double c = 0)
        {
            this.a = a;
            this.b = b;
            this.c = c;
        }
        private void GetCoefficients()
        {
            GetCoef("A", out a);
            GetCoef("B", out b);
            GetCoef("C", out c);
            void GetCoef(string letter, out double k)
            {
                do
                {
                    Console.Write($"Please, enter {letter}: ");
                } while (!double.TryParse(Console.ReadLine(), out k));
            }
        }
        private void Calculate()
        {
            double d = b * b - 4 * a * c;
            if (d > 0)
            {
                solutions = new double[2];
                solutions[0] = (-b - Math.Sqrt(d)) / (2 * a);
                solutions[1] = (-b + Math.Sqrt(d)) / (2 * a);

            }
            else if (d == 0)
            {
                solutions = new double[1];
                solutions[0] = -b / (2 * a);
            }
        }
        private void Print()
        {
            Console.Write($"Equation with A = {a}, B = {b} and C = {c} has ");
            if (solutions.Length == 0)
            {
                Console.WriteLine("no roots :(");
            }
            else if (solutions.Length == 1)
            {
                Console.WriteLine($"one root: {solutions[0]}");
            }
            else
            {
                Console.WriteLine($"two roots: {solutions[0]} and {solutions[1]}");
            }
        }
        public void Solve()
        {
            if (a == 0)
            {
                GetCoefficients();
            }
            Calculate();
            Print();
        }
    }
}
