using System.Collections;

namespace Shapes
{
    abstract class Shape: IComparable<Shape>
    {
        abstract public double GetArea();
        public int CompareTo(Shape? other)
        {
            ArgumentNullException.ThrowIfNull(other);
            return GetArea().CompareTo(other.GetArea());
        }
    }

    class Rectangle(double width, double height) : Shape, IPrint
    {
        public double Width { get; set; } = width;
        public double Height { get; set; } = height;
        public override double GetArea() => Width * Height;
        public override string ToString() => $"Rectangle with width {Width}, height {Height} and area {GetArea()}";
        public void Print() => Console.WriteLine(this);
    }

    class Square(double side) : Rectangle(side, side)
    {
        public override string ToString() => $"Square with side {Width} and area {GetArea()}";
    }

    class Circle(double radius): Shape, IPrint
    {
        public double Radius { get; set; } = radius;
        public override double GetArea() => Math.PI * Math.Pow(Radius, 2);
        public override string ToString() => $"Circle with radius {Radius} and area {GetArea()}";
        public void Print() => Console.WriteLine(this);
    }

    interface IPrint
    {
        void Print();
    }

    internal class ShapeComparer : IComparer
    {
        public int Compare(object? x, object? y)
        {
            ArgumentNullException.ThrowIfNull(x);
            ArgumentNullException.ThrowIfNull(y);
            if (x is Shape xs && y is Shape ys)
            {
                return xs.CompareTo(ys);
            }
            return 0;
        }
    }
}
