#!/usr/bin/env python
# coding: utf-8

# In[1]:


board = [['', '', ''], ['', '', ''], ['', '', '']]


# In[2]:


def print_board(board):
    for row in board:
        print('|'.join(row))


# In[3]:


def make_move(board, player):
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] == '':
                board[row][col] = player
                break
            else:
                print("That position is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")


# In[4]:


def check_win(board, player):
    # Check rows
    for row in board:
        if all(square == player for square in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == player) or             (board[0][2] == board[1][1] == board[2][0] == player):
        return True

    return False


# In[5]:


def check_tie(board):
    for row in board:
        if '' in row:
            return False
    return True


# In[6]:


def play_game():
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        player = players[current_player]
        print(f"Player {player}'s turn:")
        make_move(board, player)

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2


# In[ ]:


play_game()


# In[ ]:




