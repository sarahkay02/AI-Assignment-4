/* calc.c
 * Assignment 1
 *
 * Name: Sarah Sujin Kay
 * Email: skay@haverford.edu
 *
 * Desc: This is a simple calculator program. It asks the user for an
 *       operation (+, -, * or /), then asks for two numbers. The program
 *       then prints out the operation applied to the two numbers. It loops
 *       until the user enters 0 as the operation. 
 */

#include <stdio.h>

int main(void) {

  // declare variables
  int first_number;
  int second_number;
  char operation;

  // explain the program to the user
  printf("This program is a simple calculator.\n");

  // continue the program as long as input for operation is not zero  
  for (;;) {
	    
    // ask the user to input the operation
    printf("Enter an operation: ");
    scanf(" %c", &operation);

    // if input is zero, exit program 
    if (operation == '0') {
      break;
    }

    // if input is a character for an operation that does not exist, issue an error message
    // and continue running the program
    else if (operation != '+' && operation != '-' && operation != '*' && operation != '/') {
      printf("Invalid input. Please try again.\n");
    }

    // otherwise, continue running the program normally
    else {
      
      // ask the user to input the first number
      printf("Enter a number: ");
      scanf("%d", &first_number);

      // ask the user to input the second number
      printf("Enter a number: ");
      scanf("%d", &second_number);
    
      // calculate the result of the operation applied to the two numbers
      switch (operation) {
	// calculation will differ depending on the input (+, -, *, /)
        case '+':
	  printf("%d + %d = %d\n", first_number, second_number, first_number + second_number);
	  break;
        case '-':
	  printf("%d - %d = %d\n", first_number, second_number, first_number - second_number);
	  break;
        case '*':
	  printf("%d * %d = %d\n", first_number, second_number, first_number * second_number);
	  break;
        case '/':
	  // if second input number is zero, issue an error message and continue running the program
	  if (second_number == 0) {
	    printf("Illegal input: Can't divide by zero. Please try again.\n");
	    break;
	  }
	  else {
	    printf("%d / %d = %d\n", first_number, second_number, first_number / second_number);
	    break;
	  }
      }
    }
  }
  // when user decides to exit the program, print a good-bye message
  printf("Good-bye.\n");

  // exit the program
  return 0;
}
