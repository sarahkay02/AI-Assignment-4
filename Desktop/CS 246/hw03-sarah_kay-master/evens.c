/* evens.c
 *
 * Name: Sarah Sujin Kay
 * Desc: This program prints out the even and odd numbers that the user inputs. User can input up to 10 numbers, or stop by entering 0.
 */

 #include <stdio.h>

 int main() {
  // declare variables
  int i = 0;
  int j = 0;

  // array of 10 integers
  int numbers[10];

  // explain the program to the user
  printf("This program reads your input, and prints out the even numbers, then the odd numbers.\n");

  // ask user for input
  printf("Enter some numbers (0 to stop):\n");

  // keep going until user enters 10 numbers, or "0"
  do {
    // read and store user input
    scanf("%d", &numbers[i++]);

  } while ((i < 10) && (numbers[i-1] != 0));

  // output new-line for better spacing
  printf("\n");

  // print out even numbers
  printf("Even numbers:\n");

  for (j = 0; j < i; j++) {
    if ((numbers[j] % 2) == 0 && numbers[j] != 0) {
      printf("%d\n", numbers[j]);
    }
  }

  // output new-line for better spacing
  printf("\n");

  // print out odd numbers
  printf("Odd numbers:\n");

  for (j = 0; j < i; j++) {
    if ((numbers[j] % 2) != 0) {
      printf("%d\n", numbers[j]);
    }
  }

  // exit the program
  return 0;
 }
