// tictactoe.c, as written in Class 6
// This is a demonstration of using a two-dimensional array to
// play a simple game.

#include <stdio.h>
#include <stdbool.h>

#define BOARD_SIZE   3

// for use in the return of winner
#define NO_ONE   0
#define TIE      3

// how the state of the board is stored
#define EMPTY          0
#define X_PLAYED       1
#define O_PLAYED       2

int board[BOARD_SIZE][BOARD_SIZE];

// get the character associated with what's stored in the board
int turn_char(int xo)
{
  switch(xo)
  {
  case EMPTY:    return ' ';
  case X_PLAYED: return 'X';
  case O_PLAYED: return 'O';

  default:
    printf("Error: unexpected item in board: %d\n", xo);
    return '!';
  }
}

// print out one row
void print_row(int row)
{
  printf("%d", row); // row label
  printf(" %c ", turn_char(board[row][0])); // print out without the |
  for(int col = 1; col < BOARD_SIZE; col++)
  {
    printf("| %c ", turn_char(board[row][col]));
  }
  printf("\n");
}

// print whole board, with newlines above and below
void print_board()
{
  printf("\n");

  // column headers
  printf(" "); // room for row label
  for(int col = 0; col < BOARD_SIZE; col++)
  {
    printf(" %d  ", col);
  }
  printf("\n");

  print_row(0);  // print without the ------------ above

  for(int row = 1; row < BOARD_SIZE; row++)
  {
    printf(" ---"); // leave room for row label
    for(int col = 1; col < BOARD_SIZE; col++)
    {
      printf("+---");
    }
    printf("\n");

    print_row(row);
  }

  printf("\n");
}

// return true on successful play; false otherwise
bool play(int row, int col, int turn)
{
  if(row >= 0 && row < BOARD_SIZE && col >= 0 && col < BOARD_SIZE &&
     board[row][col] == EMPTY)
  {
    board[row][col] = turn;
    return true;
  }
  else
  {
    printf("Invalid play.\n");
    return false;
  }
}

// returns NO_ONE for no winner, X_PLAYED or O_PLAYED for a win, or TIE
// otherwise
int winner()
{
  // check for horizontal win
  for(int row = 0; row < BOARD_SIZE; row++)
  {
    int win = board[row][0];
    if(win == EMPTY)  // don't check for three EMPTYs
    {
      continue;
    }

    bool won = true;  // if we find an unequal board element, set to false
    for(int col = 1; col < BOARD_SIZE; col++)
    {
      if(board[row][col] != win)
      {
	won = false;
      }
    }

    if(won)
    {
      return win;
    }
  }

  // now for vertical win
  // NB: this could be made less repetitive, but we haven't learned enough
  // C to pull it off, yet.
  for(int col = 0; col < BOARD_SIZE; col++)
  {
    int win = board[0][col];
    if(win == EMPTY)  // don't check for three EMPTYs
    {
      continue;
    }

    bool won = true;  // if we find an unequal board element, set to false
    for(int row = 1; row < BOARD_SIZE; row++)
    {
      if(board[row][col] != win)
      {
	won = false;
      }
    }

    if(won)
    {
      return win;
    }
  }

  // top-left to bottom-right diagonal
  int win = board[0][0];
  if(win != EMPTY)
  {
    bool won = true;
    for(int i = 1; i < BOARD_SIZE; i++)
    {
      if(board[i][i] != win)
      {
	won = false;
      }
    }

    if(won)
    {
      return win;
    }
  }

  // top-right to bottom-left
  win = board[0][BOARD_SIZE-1];
  if(win != EMPTY)
  {
    bool won = true;
    for(int i = 1; i < BOARD_SIZE; i++)
    {
      if(board[i][BOARD_SIZE-1-i] != win)
      {
	won = false;
      }
    }

    if(won)
    {
      return win;
    }
  }

  // no winner. But is there a tie?
  int count_empties = 0;
  for(int row = 0; row < BOARD_SIZE; row++)
  {
    for(int col = 0; col < BOARD_SIZE; col++)
    {
      if(board[row][col] == EMPTY)
      {
	count_empties++;
      }
    }
  }

  if(count_empties == 0)
  {
    return TIE;
  }
  else
  {
    return NO_ONE;
  }
}

int main()
{
  int turn = X_PLAYED;
  int win;

  while((win = winner()) == NO_ONE)
  {
    print_board();

    int row, col; // these need to be declared out here to use in the while
    do
    {
      printf("It's %c's turn.\n", turn_char(turn));
      printf("Where would you like to play? Enter row & col: ");
      scanf("%d%d", &row, &col);

    } while(!play(row, col, turn));

    turn = X_PLAYED + O_PLAYED - turn;
  }

  print_board(); // one last time

  if(win == TIE)
  {
    printf("It's a tie. Game over.\n");
  }
  else
  {
    printf("It's %c's win!\n", turn_char(win));
  }

  return 0;
}
