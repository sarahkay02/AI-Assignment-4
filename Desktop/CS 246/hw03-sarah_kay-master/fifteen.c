/* fifteen.c
 *
 * Name: Sarah Sujin Kay
 * Desc: Allows the user to play the "Fifteen puzzle".
 */

#include <stdio.h>
#include <stdbool.h>

// representation for the empty spot in the puzzle
#define BLANK        0

// side-length of the puzzle
#define PUZZLE_SIZE  4

// global puzzle array
int puzzle[PUZZLE_SIZE][PUZZLE_SIZE]
  = { {1, 10, 15,     4},
      {13, 6,  3,     8},
      {2,  9, 12,     7},
      {14, 5, BLANK, 11} };

// prints the puzzle
void print_puzzle() {

  for (int i = 0; i < PUZZLE_SIZE; i++) {
    for (int j = 0; j < PUZZLE_SIZE; j++) {
      // print a blank space for the empty spot
      if (puzzle[i][j] == BLANK) {
        printf("\t");
      }
      else {
        // print numbers, with proper horizontal spacing
        printf("%d\t", puzzle[i][j]);
      }
    }
    // proper vertical spacing
    printf("\n\v\v");
  }
}

// prompts the user to enter a tile number and returns that number
int tile_input;

int prompt() {

  // ask the user to enter a tile number
  printf("Enter a tile number:\n");

  // read and store input
  scanf("%d", &tile_input);

  return tile_input;
}

// moves the tile in the puzzle, if possible.
void move_tile(int tile) {
  int blank_row;
  int blank_col;
  int tile_row;
  int tile_col;
  bool tile_exists = false;

  // find the position of the blank tile is (assuming the board doesn't always start the same way)
  for (int i = 0; i < PUZZLE_SIZE; i++) {
    for (int j = 0; j < PUZZLE_SIZE; j++) {
      if (puzzle[i][j] == BLANK) {
        blank_row = i;
        blank_col = j;
      }
    }
  }

  // find the position of the input tile
  for (int i = 0; i < PUZZLE_SIZE; i++) {
    for (int j = 0; j < PUZZLE_SIZE; j++) {
      if (tile == puzzle[i][j]) {
        tile_exists = true;
        tile_row = i;
        tile_col = j;
      }
    }
  }

  // if tile input doesn't exist, print an error message
  if (!tile_exists) {
    printf("Tile does not exist. Please try again.\n\n");
  }

  else {
    // check if the tile input is next to the blank space
    // check above and below
    if (tile_col == blank_col && (tile_row == blank_row + 1 || tile_row == blank_row -1)) {
      puzzle[blank_row][blank_col] = puzzle[tile_row][tile_col];
      puzzle[tile_row][tile_col] = 0;
    }

    // check to the right and left
    else if (tile_row == blank_row && (tile_col == blank_col + 1 || tile_col == blank_col - 1)) {
      puzzle[blank_row][blank_col] = puzzle[tile_row][tile_col];
      puzzle[tile_row][tile_col] = 0;
    }

    // otherwise, tile can't be moved (not next to the blank space)
    else {
      printf("Tile cannot be moved. Please try again.\n\n");
    }
  }
}

// returns true when the puzzle is solved
bool solved() {
  int k = 1;

  // loop through array and check if the numbers are in order (using k to compare the stored number and the required number)
  for (int i = 0; i < PUZZLE_SIZE; i++) {
    for (int j = 0; j < PUZZLE_SIZE; j++) {
      // check the last spot (it should be blank, and k would be 0)
      if (i == PUZZLE_SIZE-1 && j == PUZZLE_SIZE-1 && puzzle[i][j] == BLANK) {
          k = BLANK;
      }

      // if the stored number and the required number don't match, the puzzle is not solved
      if (puzzle[i][j] != k) {
        return false;
      }

      // increment k for each successive spot that is checked
      k++;
    }
  }
  return true;
}


int main() {
  // keep printing puzzle and asking for input until puzzle is solved
  while (!solved()) {
    print_puzzle();
    prompt();
    move_tile(tile_input);
  }

  // once the puzzle is solved, print finished puzzle and a message
  print_puzzle();
  printf("Puzzle solved! You won.\n");

  // exit the program
  return 0;
}
