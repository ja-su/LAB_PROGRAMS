#include<sys/types.h>
#include<unistd.h>
#include<stdio.h>
void main()
{
	int p,pid,ppid;
	p = fork();
	pid = getpid();
	ppid = getppid();
	if(p == -1)
	{
		printf("Fail");
	}
	else if(p == 0)
	{
		printf("Process:%d",getpid());
		printf("\n Parent:%d",getppid());
	}
	else
	{
		printf("Process: %d",getpid());
	}
}
	

