/* adds.c
 * Assignment 1
 *
 * Name: Sarah Sujin Kay
 * Email: skay@haverford.edu
 *
 * Desc: This program asks the user to input number and adds them together,
 *       continuing to accept numbers until the user enters a 0. It then
 *       prints the sum of the numbers.
 */

#include <stdio.h>

int main(void) {

  // declare variables
  int current_sum = 0; // set initial sum to zero
  int new_number;

  // explain the program to user
  printf("This program sums a series of integers. Enter 0 to terminate:\n");

  // ask the user to input the first number
  do
 {

    // keep track of the sum, update every time a new number is given


    // ask user for new input
    printf("Enter a number: ");
    scanf("%d", &new_number);
    current_sum += new_number;

  } while (new_number != 0);

  // print the sum once the user has entered 0
  printf("Sum: %d\n", current_sum);

  // exit the program
  return 0;
}
