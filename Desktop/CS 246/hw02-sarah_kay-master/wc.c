/* wc.c
 *
 * Name: Sarah Sujin Kay
 * Desc: This program reimplements 'wc' by reading in characters using 'getchar' and reporting how many characters, words, and lines have been read.
 */

#include <stdio.h>
#include <ctype.h>   // for isspace()
#include <stdbool.h> // for true/false

int main(void) {
  // declare variables
  int c;
  bool inside_word;

  // set counting parameters to zero
  int length = 0;
  int words = 0;
  int lines = 0;

  // explain program to the user
  printf("This program reimplements 'wc' by reading in characters, then reporting how many characters, words, and lines have been read.\n");
  printf("Type 'Ctrl + D' to terminate.\n");

  // while the user doesn't produce an EOF...
  // read and store user input
  while ( (c = getchar()) != EOF) {

    // keep count of number of characters
    length++;

    // keep count of number of words
    // if the current character is a space...
    if (isspace(c)) {
      // it's not inside a word
      inside_word = false;
    }

    else {
      // if the last character was a space...
      if (inside_word == false){
        // now you're in the middle of reading a word
        inside_word = true;
        words++;
      }
    }

    // keep count of number of lines
    if (c == '\n') {
      lines++;
    }
  }

  // print out the stats
  printf("Characters: %d\n", length);
  printf("Words: %d\n" , words);
  printf("Lines: %d\n", lines);

  // exit the program
  return 0;
}
