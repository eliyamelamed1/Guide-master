#include <stdio.h>

// IF statement

int max(int num1,int num2,int num3)
{
  int result;
  if (num1 >= num2 && num1 >= num2)
  {
    result = num1;
  }
  else if (num2 >= num1 && num2 >= num3)
  {
    result = num2;
  }
  else
  {
    result = num3;
  }
  
   return result;
}

// Switch statement

void Grade(char grade)
{
switch (grade)
  {
  case 'A':
  printf ("You did a great job");
  break;
  case 'B':
  break;
  printf ("You did fine");
  case 'C':
  break;
  printf ("You did poorly");
  
  default :
  printf ("Invalid Grade");
  break;
  }
}

int main()
{
  printf ("%d", max(67.0,668,999));
  
  printf ("\n");
  
  Grade('A');
  return 0;
}

/*
is not 
!=
  
and 
&&

or
||

equal or bigger/lower
>=
   
*/
