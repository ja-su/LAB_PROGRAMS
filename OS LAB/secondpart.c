#include<sys/types.h>
#include<stdio.h>
#include<sys/wait.h>
#include<unistd.h>
void main()
{
	int p;
	p = fork();
	if(p == -1)
	{
		printf("Fail");
	}
	else if(p == 0)
	{	
		printf("Child");
	}
	else
	{
		wait(NULL);
		printf("Parent");
	}
}
