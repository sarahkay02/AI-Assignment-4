/* triple.c
 *
 * Name: Sarah Sujin Kay
 * Desc: This program detecs a run of 3 consecutive numbers in the list of numbers that the user enters. If a run is found, then it prints out the numbers, excluding the run.
 */

#include <stdio.h>
#include <stdbool.h>

int main() {
  // array of 10 integers
  int numbers[10];

  int i = 0;
  int j = 0;
  int k = 0;
  bool consecutive[10] = {false};

  // explain program to the user
  printf("This program detects whether 3 consecutive numbers have been entered (and if so, prints out the numbers, exluding the run).\n");

  // ask user for input
  printf("Enter numbers (0 to stop):\n");

  // keep going until user enters 10 numbers, or "0"
  do {
    // read and store user input
    scanf("%d", &numbers[i++]);

  } while ((i < 10) && (numbers[i-1] != 0));


  // now, check to see if there is a run
  for (j = 0; j < i; j++) {
    if ( (numbers[j] == numbers[j+1]-1) && (numbers[j] == numbers[j+2]-2)) {
      consecutive[j] = true;
      consecutive[j+1] = true;
      consecutive[j+2] = true;
      break;
    }
  }

  for (k = 0; k < i; k++) {
    if (!consecutive[k]) {
    printf("%d\n", numbers[k]);
    }
  }

return 0;
}
