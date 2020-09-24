#include <stdio.h>

/* Creating function that returns value */
// Above main
double cube(double num)
{
  
  return num * num * num;
  // cant add code after return
}


int main()
{
  
  "Using the Functions";
  sayHi();
  
  
  sayHello("Mike", 22);
  
  printf ("Cube size is %f", cube (3.0));
  
  
  return 0;
  
  
}

/* Creating function that doesn't returns value */
// Below main


void sayHi() // Creating a Simple Function
{
  
  printf ("Hi\n");
  
}

void sayHello(char name[], int age) // Creating Function with Variable
{
  
  printf ("Hello %s, You are %d\n", name, age);
  
}
