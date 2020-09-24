#include <stdio.h>

/* Creating struct */
  
struct Student{
  
  char name [50];
  char magor [50];
  int age;
  double gpa;  
};

/* using struct */
int main()
{
  
 struct Student student1;
 student1.age = 23;
 student1.gpa = 2.8;
 // Changing value to an existing string
 strcpy (student1.name, "Eliya");
 strcpy (student1.magor, "computer science");
 
 
  return 0;
}
