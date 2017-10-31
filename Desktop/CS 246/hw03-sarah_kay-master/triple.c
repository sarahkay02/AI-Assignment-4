/* triple.c
 *
 * Name: Sarah Sujin Kay
 * Desc: This program detecs a run of 3 consecutive numbers in the list of numbers that the user enters. If a run is found, then it prints out the numbers, exluding the run.
 */

 #include <stdio.h>
 #include <stdbool.h>

 int main() {
   // array of 10 integers
   int numbers[10];

   int i = 0;
   int j;
   bool consecutive[10] = {false};

   // explain program to the user
   printf("This program detects whether 3 consecutive numbers have been entered (and if so, prints out the numbers, exluding the run).\n");

   // ask user for input
   printf("Enter numbers (0 to stop):\n");

   // keep going until user enters 10 numbers, or "0"
   do {
     // read and store user input
     scanf("%d", &numbers[i++]);

   } while ((i < 10) && (numbers[i-1] != 0));


   // now, check to see if there is a run
   for (j = 0; j < i; j++) {

     // if the current number, and the next two, are consecutive...
     if ((numbers[j] == numbers[j+1]-1) && (numbers[j] == numbers[j+2]-2)) {

       // mark these three numbers as consecutive
       consecutive[j] = true;
       consecutive[j+1] = true;
       consecutive[j+2] = true;

       // we only need to find the first occurrence
       break;
     }
   }

   // output new-line for better spacing
   printf("\n");

   // if a run is found...
   if (consecutive[j]) {
     printf("Run found.\n");

     // print out all the numbers in the array that aren't consecutive
     for (j = 0; j < i; j++) {
       if (!consecutive[j] && numbers[j] != 0) {
         printf("%d\n", numbers[j]);
       }
     }
   }

   // otherwise, tell the user that no run was found
   else {
     printf("No run found.\n");
   }

   // exit the program
   return 0;
 }
