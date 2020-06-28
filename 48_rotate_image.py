class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix[0])
        # создать матрицу равной размерности для дальнейшего заполнения
        new_matrix = [[None for n in range(0, size)] for line in range(0, size)]
        previous_line_number = -1
        for line_num, line in enumerate(matrix):
            for column_num, cell in enumerate(line):
                # посчитать дельту, на которую будет изменяться x-координата в y-координату
                delta = size - (line_num + 1) - (previous_line_number + 1)
                new_matrix[column_num].pop(line_num + delta)
                new_matrix[column_num].insert(line_num + delta, cell)
            previous_line_number = line_num
        for line_num, line in enumerate(new_matrix):
            for column_num, cell in enumerate(line):
                matrix[line_num][column_num] = cell
