/* matrix.c

   Name: Sarah Sujin Kay
   Resources used (websites, books other than our texts, peers):

*/

#include "matrix.h"

// checks to see if two NxM matrices are the same
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

// prints an NxM matrix
void print_matrix(int n, int m, int mat[n][m]) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      printf("%d\t", mat[i][j]);
    }
    printf("\n\v");
  }
}

// fills in an NxN matrix with the identity matrix
void identity_mat(int n, int mat[n][n]) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (i == j) {
        mat[i][j] = 1;
      }
      mat[i][j] = 0;
    }
  }
}

// multiplies an NxM matrix by a scalar; stores the result in `result`
void scalar_mult(int scalar, int n, int m, int mat[n][m], int result[n][m]) {



}

// multiplies an N1xM1 matrix by a M1xM2 matrix, storing the result in `result`
void matrix_mult(int n1, int m1, int mat1[n1][m1],
                 int m2, int mat2[m1][m2],
                 int result[n1][m2]) {



}

// Exponentiate an NxN matrix. The result is stored in `result`.
void matrix_pow(int n, int mat[n][n], int power, int result[n][n]) {



}

// Exponentiate an NxN matrix. The result is stored in `result`.
void matrix_pow_rec(int n, int mat[n][n], int power, int result[n][n]) {



}
