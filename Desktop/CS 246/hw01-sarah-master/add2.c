/* add2.c
 * Assignment 1
 *
 * Name: Sarah Sujin Kay
 * Email: skay@haverford.edu
 *
 * Desc: This program asks the user for two numbers, then prints their sum.
 */

#include <stdio.h>

int main(void) {

  // declare variables
  int first_number;
  int second_number;
  int sum;

  // explain the program to the user
  printf("This program gives the sum of two integers.\n");
  
  // asks the user to input first number
  printf("Enter a number: ");
  scanf("%d", &first_number);

  // asks the user to input second number
  printf("Enter a number: ");
  scanf("%d", &second_number);

  // add the two numbers
  sum = first_number + second_number;

  // print the sum of the numbers
  printf("%d + %d = %d\n", first_number, second_number, sum);

  // exit the program
  return 0;
}
  
  
