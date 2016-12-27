#! /usr/bin/local/python3

# 1. Print out cheesy welcome
print("Welcome to tic-tac-toe profession v0.1")
print()

# 2. setup game data structures
x = 1
o = -1
e = 0
game = [
    [e, e, e],
    [e, e, e],
    [e, e, e],
]

# 3. Print the empty board (will require two for loops)
#     Convert value of x => 'x'
#     Convert value of o => 'o'
#     Convert value of e (empty) => '.'

print("The board is set:")
for row in game:
    for c in row:
        print('x' if c == x else ('o' if c == o else '.'), end=' ')
    print()
print()

# 4. Setup game loop variables
#     this includes: turn, winner, and hasWon.
turn = 1
activeValue = None
winner = None
hasWon = False

# 5. Game loop (while loop until someone has won):

while not hasWon:
    # 5.1 print who's turn it is (X or O)
    if turn == 1:
        activeValue = x
        print("It's X's turn.")
    else:
        activeValue = o
        print("It's Y's turn.")

    #   5.2 ask user for row (via input('prompt text'), convert to int via int(text))
    row = int(input("Choose row (zero based): "))
    #   5.3 ask user for column (same)
    col = int(input("Choose column (zero based): "))

    #   5.4 verify row and column are in bounds
    #   5.5 verify that entry is not already chosen
    if not game[row][col] == e:
        print("Sorry, that position is already occupied with a {0}!".format(game[row][col]))
        print("try again")
        for row in game:
            for c in row:
                print('x' if c == x else ('o' if c == o else '.'), end=' ')
            print()

        print()
        continue

    #   5.6 set row/column to correct value (e.g. game[row][column] = x)
    game[row][col] = activeValue

    #   5.7 show the board again (now that it's updated)
    print("Excellent choice:")
    for row in game:
        for c in row:
            print('x' if c == x else ('o' if c == o else '.'), end=' ')
        print()

    print()
    print("We're checking for a winner...")

    #   5.8 check for a winner (any row or diagonal sums to 3 => x's win, -3 => o's win)
    row1 = game[0][0] + game[0][1] + game[0][2]
    row2 = game[1][0] + game[1][1] + game[1][2]
    row3 = game[2][0] + game[2][1] + game[2][2]
    col1 = game[0][0] + game[1][0] + game[2][0]
    col2 = game[0][1] + game[1][1] + game[2][1]
    col3 = game[0][2] + game[1][2] + game[2][2]
    diag1 = game[0][0] + game[1][1] + game[2][2]
    diag2 = game[0][2] + game[1][1] + game[2][0]

    if row1 == 3 or row2 == 3 or row3 == 3 or col1 == 3 or \
                    col2 == 3 or col3 == 3 or diag1 == 3 or diag2 == 3:
        hasWon = True
        winner = "X"

    if row1 == -3 or row2 == -3 or row3 == -3 \
            or col1 == -3 or col2 == -3 or col3 == -3 or diag1 == -3 or diag2 == -3:
        hasWon = True
        winner = "O"

    if not hasWon:
        print("No winner yet, keep going!")
        print()

    #   5.9 switch players, repeat.
    turn *= -1

# 6. Announce winner and show the winning board.

print("We have a winner! It's the " + winner + "'s!")
print("Way to win the day")
print()
for row in game:
    for c in row:
        print('x' if c == x else ('o' if c == o else '.'), end=' ')
    print()