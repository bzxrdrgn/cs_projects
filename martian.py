import os
import random

def create_matrix():
    return [[' ' for _ in range(7)] for _ in range(7)]

def place_ships(matrix):
    # Place ships of different sizes
    for size in [3, 2, 2, 1, 1, 1, 1]:
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x, y = random.randint(0, 6-size), random.randint(0, 6)
            else:
                x, y = random.randint(0, 6), random.randint(0, 6-size)
            
            if all(matrix[y+dy][x+dx] == ' ' for dx in range(size) for dy in (-1, 0, 1) for dx in (-1, 0, size)):
                for dx in range(size):
                    matrix[y][x+dx] = 'S'
                break

def display_matrix(matrix, reveal=False):
    for row in matrix:
        for cell in row:
            if cell == 'S' and not reveal:
                print(' ', end=' ')
            elif cell == ' ':
                print('~', end=' ')
            elif cell == 'H':
                print('X', end=' ')
            elif cell == 'M':
                print('O', end=' ')
        print()

def take_shot(matrix, x, y):
    if matrix[y][x] == 'S':
        matrix[y][x] = 'H'
        if all(cell != 'S' for row in matrix for cell in row):
            return 'win'
        else:
            return 'hit'
    else:
        matrix[y][x] = 'M'
        return 'miss'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    matrix = create_matrix()
    place_ships(matrix)
    shots = 0
    while True:
        clear_console()
        display_matrix(matrix)
        x = int(input('Enter x coordinate: '))
        y = int(input('Enter y coordinate: '))
        result = take_shot(matrix, x, y)
        shots += 1
        if result == 'win':
            clear_console()
            display_matrix(matrix, reveal=True)
            print(f'You won with {shots} shots!')
            return shots

def main():
    scores = []
    while True:
        name = input('Enter your name: ')
        scores.append((name, play_game()))
        scores.sort(key=lambda x: x[1])
        if input('Do you want to play again? (yes/no) ') != 'yes':
            for name, score in scores:
                print(f'{name}: {score}')
            break

if __name__ == '__main__':
    main()
    