#include <stdio.h>
#include <stdbool.h>

// representation for the empty spot in the puzzle
#define BLANK        0

// side-length of the puzzle
#define PUZZLE_SIZE  4

// declare variables
int i;
int j;
bool in_order = false;

// global puzzle array
int puzzle[PUZZLE_SIZE][PUZZLE_SIZE]
  = { {1, 2, 3, 4},
      {5, 6,  7, 8},
      {9,  10, 11, 12},
      {13, 14, 15, BLANK} };

// prints the puzzle


// prompts the user to enter a tile number and returns that number
int prompt() {
  int tile_input;
  printf("Enter a tile number:\n");
  scanf("%d", &tile_input);

  return tile_input;
}


// returns true when the puzzle is solved
bool solved() {
  int k = 1;

  for (i = 0; i < PUZZLE_SIZE; i++) {
    for (j = 0; j < PUZZLE_SIZE; j++) {
      // loop through array and check if the numbers are in order (if each successive number is one smaller than the next)
      if (i == PUZZLE_SIZE-1 && j == PUZZLE_SIZE-1) {
        if (puzzle[i][j] == BLANK) {
          k = 0;
        }
      }
      if (puzzle[i][j] == k) {
        in_order  = true;
        printf("K: %d, IJ: %d, True?: %d\n", k, puzzle[i][j], in_order);
      }
      else {
        in_order = false;
        printf("Else: %d, IJ: %d, True?: %d\n", k, puzzle[i][j], in_order);
      }
      k++;
    }
  }
      return (in_order);
    }


int main() {
  // keep asking for input until puzzle is solved
  while (!solved()) {
    prompt();
  }

  // once the puzzle is solved, print finished puzzle and a message
  printf("Puzzle solved! You won.\n");

  // exit the program
  return 0;
}
