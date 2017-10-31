// Driver program
#include <stdio.h>

#include "func.h"

int main() {
  printf("Enter two numbers and I'll add them:\n");
  int i, j;
  scanf("%d%d", &i, &j);

  printf("Sum: %d", sum(i, j));

  return 0;
}
