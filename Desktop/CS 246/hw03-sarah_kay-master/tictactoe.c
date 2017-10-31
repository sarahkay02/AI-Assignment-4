#define BOARD_SIZE  3

#define NO_ONE      0
#define TIE         1
#define X_WINS      2
#define O_WINS      3

#define EMPTY       0
#define X_PLAYED    1
#define O_PLAYED    2

// defined a global variable, outside of any function
int board[BOARD_SIZE][BOARD_SIZE];

// in C, everything has to be defined in order
int winner () {
  // four different things this might return
  // WRITE ME
  // detect 3 in a row
}

void print_board() {
  // WRITE ME
}

// return true on successful play, false otherwise
bool play(int row, int col, int turn) {
  // WRITE ME
}



int main() {
  // keep track of who's turn it is
  int turn = X_PLAYED;

  while(winner() == NO_ONE) {
    // print the board
    print_board();

    do {
    // ask the user for the next move
    int row, col;
    printf("Where do you want to play? Enter row % col: ");
    scanf("%d%d", &row, &col);
    // will return true if your move is valid/succeeds
  } while (!play(row, col, turn));

    // if(turned == X_PLAYED) {
    //  turn = O_PLAYED
    // }
    turn = X_PLAYED + O_PLAYED - turn;
  }

  // tell who wins
  report_winner();
}
