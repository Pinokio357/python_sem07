num_rows = 6
num_colums = 6
operation = lambda x,y: x * y

def print_operation_table(function, r, c):
    for row in range(1, r + 1):
        for colum in range(1, c + 1):
            print(function(row, colum), end="\t")

        print()

print_operation_table(operation, num_rows, num_colums)
