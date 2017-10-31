/* scream.c
 *
 * Name: Sarah Sujin Kay
 * Desc: This program mimicks 'cat' behavior by printing out precisely what is read in, but additionally changes all letters to uppercase bit-flicking operations.
 */

#include <stdio.h>
#include <ctype.h>   // for islower

// the difference between lower-case and upper-case letters is 32 (2^5), which corresponds to the 'space' character (using the ASCII table).
#define KEY ' '

int main(void) {
  // declare variables
  char c;

  // explain the program to the user
  printf("This program mimics 'cat' behavior by repeating what it reads in, except it changes all letters to uppercase.\n");
  printf("Type 'Ctrl + D' to terminate.\n");

  // while the user doesn't produce an EOF...
  // read and store user input
  while ( (c = getchar()) != EOF) {

    // only convert if the character is alphabetical and lower-case (we don't want to change characters that are already upper-case, or are digits/symbols)
    if (islower(c)) {
      // XOR each character using the 'space' character to convert to upper-case
      c = c ^ KEY;
    }

    // print the final output, in all upper-case
    putchar(c);
  }

  // exit the program
  return 0;
}
