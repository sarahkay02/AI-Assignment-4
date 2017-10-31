#include <stdio.h>
#include "sum.h"

int added;

int sum (int i, int j) {
  added = i + j;
  printf("%d", added);
}
