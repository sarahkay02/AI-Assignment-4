
#include <stdio.h>
#include <stdbool.h>

void identity_mat(int n) {
  int mat[n][n];
  int i;
  int j;
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      if (i == j) {
        mat[i][j] = 1;
      }
      else {
        mat[i][j] = 0;
      }
      printf("%d\t", mat[i][j]);

    }
    printf("\n");
  }
}



int main() {
  int n;
  int mat[5][5];
  identity_mat(5);
}
