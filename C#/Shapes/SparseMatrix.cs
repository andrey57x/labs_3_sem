using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Shapes
{
    internal class SparseMatrix<T>
    {
        private Dictionary<int[], T> matrix;
        public SparseMatrix()
        {
            matrix = [];
        }
        public T this[int k1, int k2, int k3]
        {
            get
            {
                foreach (int[] i in matrix.Keys)
                {
                    if (i[0] == k1 && i[1] == k2 && i[2] == k3)
                    {
                        return matrix[i];
                    }
                }
                throw new KeyNotFoundException("Нет такого");
            }
            set
            {
                matrix[[k1, k2, k3]] = value;
            }
        }
    }
}
