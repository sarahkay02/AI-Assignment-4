/* cat.c
 *
 * Name: Sarah Sujin Kay
 * Desc: This program mimics the behavior of the command-line tool 'cat', by printing out precisely what is read in.
 */

#include <stdio.h>

int main(void) {
  // declare variables
  char c;

  // explain the program to the user
  printf("This program mimics 'cat' behavior by repeating what it reads in.\n");
  printf("Type 'Ctrl + D' to terminate.\n");

  // while the user doesn't produce an EOF...
  // read user input
  while ( (c = getchar()) != EOF) {
    // print out what was read in
    putchar(c);
  }

  // exit the program
  return 0;
}
