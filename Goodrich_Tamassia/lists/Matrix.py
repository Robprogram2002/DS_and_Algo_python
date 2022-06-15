class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0] * cols for j in range(rows)]
        self.dim = (rows, cols)

    def __getitem__(self, i):
        if 0 <= i[0] < self.dim[0] and 0 <= i[1] < self.dim[1]:
            return self.matrix[i[0]][i[1]]
        else:
            raise IndexError

    def __len__(self):
        return self.dim[0] * self.dim[1]

    def __setitem__(self, key, value):
        if 0 <= key[0] < self.dim[0] and 0 <= key[1] < self.dim[1]:
            self.matrix[key[0]][key[1]] = value
        else:
            raise IndexError

    def print_matrix(self):
        for k in range(self.dim[0]):
            print(self.matrix[k])

    def get_dim(self):
        return self.dim

    def sum_cells(self):
        # comprehension syntax implementation (flattening the nested list)
        return sum(val for row in self.matrix for val in row)

        # loop implementation

        # sum_total = 0
        # for k in range(self.dim[0]):
        #     for j in range(self.dim[1]):
        #         sum_total += self.matrix[k][j]
        # return sum_total

    def sum_cells_recursive(self, row):
        print('next')

    def __add__(self, other):
        new_matrix = Matrix(self.dim[0], self.dim[1])
        if isinstance(other, (int, float)):
            for k in range(self.dim[0]):
                for j in range(self.dim[1]):
                    new_matrix[[k, j]] = self.matrix[k][j] + other
        elif isinstance(other, Matrix) and other.get_dim() == self.get_dim():
            for k in range(self.dim[0]):
                for j in range(self.dim[1]):
                    new_matrix[[k, j]] = self.matrix[k][j] + other[[k, j]]
        else:
            raise TypeError('matrix only can add an scalar value or another matrix with the same dimensions')

        return new_matrix

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Only can multiply by other matrix')
        elif self.dim[1] != other.dim[0]:
            raise ValueError('Matrix not agree in dimensions')
        new_matrix = Matrix(self.dim[0], other.dim[1])
        for j in range(self.dim[0]):
            for i in range(other.dim[1]):
                total = 0
                for k in range(self.dim[1]):
                    total += self.matrix[j][k] * other[[k, i]]
                new_matrix[[j, i]] = total

        return new_matrix


if __name__ == '__main__':
    matrix_A = Matrix(3, 4)
    matrix_A.print_matrix()
    matrix_A[[1, 2]] = 100
    print('-----------------')
    matrix_A.print_matrix()
    print(matrix_A[[1, 2]])
    print('-----------------')
    matrix_B = matrix_A + 3.25
    matrix_A += 3
    matrix_B.print_matrix()
    matrix_B = matrix_A + matrix_A
    matrix_B.print_matrix()
    print(matrix_B.sum_cells())
    print('......................')
    matrix_A = Matrix(3, 3) + 3
    matrix_A.print_matrix()
    matrix_B.print_matrix()
    mult_mat = matrix_A * matrix_B
    mult_mat.print_matrix()
