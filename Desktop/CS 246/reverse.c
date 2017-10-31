#
#include <stdio.h>

int leftover;
int printout;

int reverse_digits(int n) {
  while (leftover > 0) {
    printout = leftover % 10;
    printf("%d", printout);

  }


return printout;
}


int main() {
  printf("Enter some numbers:\n");
  reverse_digits(206);


  // exit the program
  return 0;
}
