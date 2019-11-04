#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

int main() { 
 pid_t pid; 
 int value = 100; 
 value += 5;  
 pid = fork();
 
 if(pid==0) { 
  value += 30; 
  printf("Child: pid = %d value = %d\n", getpid(), value); 
 } 
 else if(pid>0) {  
  wait(NULL); 
  value +=25; 
  printf("Parent: pid = %d value = %d\n", getpid(), value); 
 } 
 return 0; 
} 
