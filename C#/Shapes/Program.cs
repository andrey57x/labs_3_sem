using System.Collections;

namespace Shapes
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Lab2:");
            Lab2();
            Console.WriteLine("\nLab3:");
            Lab3();
        }
        static void Lab2()
        {
            Rectangle rectangle = new(10.5, 11.25);
            Rectangle square = new Square(10.5);
            Circle circle = new(10);
            rectangle.Print();
            square.Print();
            circle.Print();
        }

        static void Lab3()
        {
            ArrayList arrayList = [(Shape)new Rectangle(9, 11), (Shape)new Square(8), (Shape)new Circle(5)];
            Console.WriteLine("Array:");
            Print(arrayList);
            arrayList.Sort(new ShapeComparer());
            Console.WriteLine("Sorted array:");
            Print(arrayList);
            List<Shape> list = [new Square(5), new Rectangle(4, 7),  new Circle(2)];
            Console.WriteLine("List:");
            Print(list);
            list.Sort();
            Console.WriteLine("Sorted list:");
            Print(list);
            SparseMatrix<Shape> sparseMatrix = new();
            sparseMatrix[1, 2, 3] = new Rectangle(2, 5);
            sparseMatrix[2, 4, 7] = new Circle(2);
            sparseMatrix[3, 9, 3] = new Square(3);
            Console.WriteLine("SparseMatrix: " + sparseMatrix[3, 9, 3].ToString() + ' ' + sparseMatrix[2, 4, 7].ToString() + ' ' + sparseMatrix[1, 2, 3].ToString());
        }

        static void Print(IList objects) {
            foreach (var obj in objects)
            {
                Console.WriteLine(obj);
            }
        }
    }
}
