#include <stdio.h>

//Compiler version gcc  6.3.0

int main()
// %p (pointer) 
// print the memory adress of the variable
{
  
  int age = 1002;
  
  int *page = &age; // Saving age memory location to varaible
 
  printf ("the memory location of age is: %p \nthe value at page memory location is: %d", &page,*page);
  
  
}
