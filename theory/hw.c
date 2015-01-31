#include <stdio.h>
#include <stdlib.h>

void ToH(char source, char dest,char spare, int n);
void ToHRecursive(char source, char dest, char spare, int n, int disk);


int main(int argc, const char* argv[]){
  if (argc == 2){
    int n = atoi(argv[1]);
    ToH('a','b','c',n);
  }
  else if (argc == 5){
    ToH(*argv[1], *argv[2], *argv[3], atoi(argv[4]));
  }
  else {
    printf("Please supply %s with either a number of discs or names for"
	   "the poles and the number of discs\n", argv[0]);
  }
}
void ToH(char source, char dest, char spare, int n){
  ToHRecursive(source, dest, spare, n, n);
}
void ToHRecursive(char source, char dest, char spare, int n, int disk){
  if (n==1){
    static cnt = 1;
    printf("%d.Move disk %d  from %c to %c. \n", cnt, disk, source, dest);
    cnt +=1;
  } else {
    ToHRecursive(source, spare, dest, n-1, disk-1);
    ToHRecursive(source, dest, spare, 1, disk);
    ToHRecursive(spare, dest, source, n-1, disk-1);
  }
}
/*
oliver@oliver-XPS:~/TPOP/theory$ ./hw5 3
1.Move disk 1  from a to b. 
2.Move disk 2  from a to c. 
3.Move disk 1  from b to c. 
4.Move disk 3  from a to b. 
5.Move disk 1  from c to a. 
6.Move disk 2  from c to b. 
7.Move disk 1  from a to b. 

oliver@oliver-XPS:~/TPOP/theory$ ./hw5 13 | grep 100
100.Move disk 3  from a to b. 

oliver@oliver-XPS:~/TPOP/theory$ ./hw5 13 | grep disk' '12
2048.Move disk 12  from a to c. 
6144.Move disk 12  from c to b. 


 */
