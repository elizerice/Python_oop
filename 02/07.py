class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            return None

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        self.data.pop(row)
        self.rows -= 1

    def delete_col(self, col):
        for row in self.data:
            row.pop(col)
        self.cols -= 1

    def add_row(self, row):
        self.data.insert(row, [0] * self.cols)
        self.rows += 1

    def add_col(self, col):
        for row in self.data:
            row.insert(col, 0)
        self.cols += 1
