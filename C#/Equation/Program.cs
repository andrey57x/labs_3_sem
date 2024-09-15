class Program
{
    static void Main(string[] args)
    {
        Equation.Equation equation = new();
        if (args.Length > 0)
        {
            equation.SetCoefs(Convert.ToDouble(args[0]), Convert.ToDouble(args[1]), Convert.ToDouble(args[2]));
        }
        equation.Solve();
    }
}
