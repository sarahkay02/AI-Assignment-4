#
#include <stdio.h>

int main() {
  // declare variables
  int nums;
  int numbers[10];
  int i = 0;
  int j = 0;

  printf("Enter some numbers:\n");

  scanf("%d", &nums);

  while(i < 10 && nums != 0) {
    numbers[i] = nums;
    i++;
    scanf("%d", &nums);
  }

  printf ("\n");

  // print out what was read in
  for (j = 0; j < i; j++) {
    printf("%d\n", numbers[j]);
  }

  printf("\n");

  // print out in reverse
  for(i--; i >= 0; i--) {
    printf("%d\n", numbers[i]);
  }

  printf("\n");

  // exit the program
  return 0;
}
