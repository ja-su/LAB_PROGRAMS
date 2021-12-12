#include<stdio.h>
#include<sys/types.h>
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
		execlp("./second","second",NULL);
	}
	else
	{
		printf("hello");
	}
}
