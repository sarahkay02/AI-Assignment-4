/* shout.c
 *
 * Name: Sarah Sujin Kay
 * Desc: This program mimicks 'cat' behavior by printing out precisely what is read in, but additionally changes all letters to uppercase using arithmetic.
 */

#include <stdio.h>
#include <ctype.h>   // for isalpha

int main(void) {
  // declare variables
  char c;

  // explain the program to the user
  printf("This program mimics 'cat' behavior by repeating what it reads in, except it changes all letters to uppercase.\n");
  printf("Type 'Ctrl + D' to terminate.\n");

  // while the user doesn't produce an EOF...
  // read and store user input
  while ( (c = getchar()) != EOF) {
    // check if character is alphabetic
    if (isalpha(c)) {
      // if lower-case, convert to uppercase (otherwise, no change)
      if ('a' <= c && c <= 'z') {
        c = c - 'a' + 'A';    // or do: c = c - 32;
      }
    }
    // print out upper-case version of input
    putchar(c);
  }

  // exit the program
  return 0;
}
