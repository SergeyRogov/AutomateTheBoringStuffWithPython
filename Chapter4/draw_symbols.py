def draw_symbols(matrix):
    for i in range(len(matrix[0])):
        for j in reversed(range(len(matrix))):
            print(matrix[j][i], end=' ')
        print()

def main():
    grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]
    draw_symbols(grid)