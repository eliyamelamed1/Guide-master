#include <stdio.h>

//Compiler version gcc  6.3.0

int main()
{

  "Creating Array";
 /* type name [size] = {values}; */
 // size and *values are optional 
 int array [2] = {7,8};
 
  "Adding / Modifying array";
 /* array[index] = value: */
 array [3] = 2;
 
 "Printing & accessing Array Values";
 /* printf ("%type", array [index]) */
 printf ("%d", array [3]);
 
 
 "2D Array";
 int nums[3][2] = 
   {
     {1,2},
     {3,4},
     {5,6},
   };
   printf ("\n2D Array values: %d", nums[0][1]);
 
  
}
