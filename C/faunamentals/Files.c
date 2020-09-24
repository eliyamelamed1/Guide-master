#include <stdio.h>

//Compiler version gcc  6.3.0

// r - read
// a - append
// w - writed


int main()
{
  FILE * fpointer (file_name.txt, 'w');
 
  fprintf (fpointer, 'you can write whatever you want');
  
  fclose (fpointer);
}
