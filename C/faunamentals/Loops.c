#include <stdio.h>

//Compiler version gcc  6.3.0

int main(){
  
  int index = 1;
  
  /* While loop */
  // Checking the condition 
  // if True executes the code
  while (index <= 3)
  {
    printf ("\nWHILE LOOP\n");
    printf ("index value is: %d\n", index);
    index += 1;
  }
  
  
  /* Do loop */
  // always executes the code for the first time
  // and then check condition
  do 
  {
    printf ("\nDO LOOP\n");
    printf ("index value is: %d\n", index);
    index += 1;
    
  }while (index <= 3);
  
  /* For loop */
  
  int i;
  for (i = 1 ; i < 4 ; i += 1)
  {
    printf ("\nFOR LOOP\n");
    printf ("i value is: %d\n", i);
    
  }
  
  
  
  return 0;
}
