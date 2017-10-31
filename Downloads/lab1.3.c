#include <stdio.h>

int main(void) {
  float x = 5.290009901;
  x = (double)x;
  x = (float)x;
  printf("%g", x);
}
