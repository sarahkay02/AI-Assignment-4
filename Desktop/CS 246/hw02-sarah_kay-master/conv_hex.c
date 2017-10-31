/* conv_hex.c
 *
 * Name: Sarah Sujin Kay
 * Desc: This program converts a number in hexadecimal to octal. Both
 *       the input and output are reversed.
 */

#include <stdio.h>

int main(void) {
  // declare variables
  char c;
  int decimal;
  int _remainder = 0;
  int carry = 0;
  int power_of_two = 1;

  // explain the program to the user
  printf("This program converts a number from hexadecimal to octal.\n");

  // ask the user for input
  c = getchar();

  while (1) {

    // exit the program if the quotient (carry value) is zero, and input == '\n'. This is when you know you've completed the conversion.
    if (carry == 0 && c == '\n') {
      break;
    }

    // if the character is the new-line, then print the carry value (converted to a decimal), then break
    if (c == '\n') {
      putchar(carry + '0');
      break;
    }

    // if the character is a letter A-F (using ASCII table), convert to decimal value
    if (c >= 65) {
      // number = converted * 2^n + carry value
      decimal = (c - 55) * power_of_two + carry;
    }
    else {
      decimal = (c - 48) * power_of_two + carry;
    }

    // calculate the remainder when dividing decimal by 8
    _remainder = decimal % 8;

    // calculate the quotient (which is what you carry over to the next computation)
    carry = decimal/8;

    // print out the remainder (this is what is going to build the octal number)
    putchar(_remainder + '0');

    // increment 2^n to 2^(n+1)
    power_of_two *= 2;

    // read next character
    c = getchar();
  }

  // output a new-line before exiting
  putchar('\n');
  
  // exit the program
  return 0;
}
