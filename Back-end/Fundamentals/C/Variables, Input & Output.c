#include <stdio.h>

//Compiler version gcc  6.3.0

int main()
{ 
   
  /* Variable and Output types */
  int number = 40; // intergar
  printf ("my number is %d \n", number);
  
  double gpa = 3.6; // decimal
  printf ("my gpa is %f \n", gpa);
  
  char phrase ['size'] = "Tutorial"; // String
  printf ("my gpa is %s \n", phrase);
  
  char digit = 'A'; // Single letter
  printf ("my digit is %c \n", digit);
  
  /* Determine string length */
  char stringlength[size];
    
  /* Permanent variable - Cant be changed */
  const int NUM = 10;
  
  /* User Input */
  int age;
  printf ("enter your age: ");
  scanf ("%d", &age);
  printf ("you are %d years old", age);
  
  double decimal;
  printf ("enter decimal: ");
  scanf ("%lf", &decimal);
  printf ("you decimal is: %f", decimal);
  
  char grade; // Single digit
  printf ("enter grade: ");
  scanf ("%c", grade);
  
  char country[];// String
  printf ("enter your country: ");
  scanf ("%s", country);
  
  /* Getting string input (that doesnt stop after space) */
  char name[20];
  printf ("enter your name: ");
  fgets (name, 20, stdin);
  printf ("you name is: %s", name);
 
  
  return 0;
}
