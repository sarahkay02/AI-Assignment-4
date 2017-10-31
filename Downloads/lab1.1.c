// Name: Sarah Sujin Kay
// Desc: Lab 1

// Write C code to figure out how many bytes are taken up by the following
// types on your machine:

#include <stdio.h>

int main(void) {
  printf("Size of int: %zu\n", sizeof(int));
  printf("Size of short: %zu\n", sizeof(short));
  printf("Size of long: %zu\n", sizeof(long));
  printf("Size of char: %zu\n", sizeof(char));
  printf("Size of float: %zu\n", sizeof(float));
  printf("Size of double: %zu\n", sizeof(double));

  // exit the program
  return 0;
}
