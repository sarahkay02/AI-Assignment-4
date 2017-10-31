/* fifteen.c
 *
 * Name:
 * Desc: Allows the user to play the "Fifteen puzzle"
 */

#include <stdio.h>
#include <stdbool.h>

// These lines define constants which can be used throughout your program
// to aid in your code. They are explained on p. 315 of King and have a
// nice introduction on this page:
// http://www.dummies.com/programming/c/how-to-declare-and-use-constants-in-the-c-language/

// representation for the empty spot in the puzzle
#define BLANK        0

// side-length of the puzzle
#define PUZZLE_SIZE  4 

// arrays do strange and wonderful things when passed as parameters, so we'll just
// use a global variable. This puzzle variable is accessible anywhere in your program.
int puzzle[PUZZLE_SIZE][PUZZLE_SIZE]
  = { {1, 10, 15,     4},
      {13, 6,  3,     8},
      {2,  9, 12,     7},
      {14, 5, BLANK, 11} }; // global puzzle array

// the functions below are a suggestion for a way to write this assignment, though
// they are not a requirement

// prints the puzzle
void print_puzzle()
{
  // WRITE ME!
}

// prompts the user to enter a tile number and returns that number
int prompt()
{
  // WRITE ME!
}

// moves the tile in the puzzle, if possible.
void move_tile(int tile)
{
  // WRITE ME!
}

// returns true when the puzzle is solved
bool solved()
{
  // WRITE ME!
}

int main()
{
  // WRITE ME!

  return 0;
}
