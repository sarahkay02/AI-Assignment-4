
#include <stdio.h>

bool eq_matrix(int n, int m, int mat1[n][m], int mat2[n][m]) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (mat1[i][j] != mat2[i][j]) {
        return false;
      }
    }
  }
  return true;
}



int main() {
  int mat1 = { 1, 2, 3, 4, 5, 6 };
  int mat2 = { 1, 2, 3, 4, 5, 6 };

  eq_matrix(2, 3, mat1, mat2);
}
