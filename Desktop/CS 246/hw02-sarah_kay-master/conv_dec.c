/* conv_dec.c
 *
 * Name: Sarah Sujin Kay
 * Desc: This program converts a number from decimal to hexadecimal. Output is reversed.
 */

#include <stdio.h>
#include <stdbool.h> // for true/false

int main(void) {
  // declare variables
  char c;
  int decimal = 0;
  int hex;
  int _remainder;

  // explain program to user
  printf("This program converts a number from decimal to hexadecimal.\n");

  // read input as characters
  while ( (c = getchar()) != '\n') {
    // c - '0' will convert the character to a numerical digit
    // each time a new character is inputted, multiply each digit by 10 to "push" it to the left
    decimal = (decimal*10) + (c - '0');
  }

  // now, convert decimal to hex
  while (decimal != 0) {
    // calculate the remainder when dividing number by 16
    _remainder = decimal % 16;

    // if the quotient is >= 10, you need to convert to a letter character (using ASCII table)
    if (_remainder >= 10) {
      _remainder = _remainder + 55;
    }

    // otherwise, convert to a number character
    else {
      _remainder = _remainder + 48;
    }

    // print the resulting character
    putchar(_remainder);

    // divide decimal number by 16
    decimal = decimal/16;
  }

  // output a new-line before exiting
  putchar('\n');

  // exit the program
  return 0;
}
