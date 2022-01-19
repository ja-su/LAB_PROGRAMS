#include<stdio.h>
#include<stdlib.h>

struct process{
int pid;
int at;
int wt;
int tat;
int bt;
int ct;
}
p[20],temp;

int n,tq;
float avwt,avtat;

void display()
{

	int i;
	printf("Process ID\tArrival Time\tBurst Time\tWaiting Time\t\tTurnaround Time\n");

	for(i = 0; i < n; i++)    
		printf("%d\t\t%d\t\t%d\t\t%d\t\t\t%d\n", p[i].pid, p[i].at, p[i].bt, p[i].wt, p[i].tat);

	printf("\nAverage Waiting Time: %f", avwt);
	printf("\nAverage Turnaround Time: %f\n", avtat);

}

void swap(int i, int j) //swapping elements
{
	temp=p[i];
 	p[i]=p[j];
 	p[j]=temp;
}

void atSort() //sorting arriving time
{
	int i,j;
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-i-1;j++)
 		{
  			if(p[j].at>p[j+1].at)    
  			{
    				swap(j,j+1); 
  			}
 		}
	}
}

void pidSort() //sorting the process id
{
 	int i,j;	
 	for(i=0;i<n-1;i++)
 	{
  		for(j=0;j<n-i-1;j++)
   		{
    			if(p[j].pid>p[j+1].pid)    
    			{
      				swap(j,j+1); 
    			}
  		}
 	}
}

void fcfs()
{

	int i;	

	atSort(); 

	p[0].ct = p[0].at + p[0].bt;
	p[0].tat = p[0].ct - p[0].at;
	p[0].wt = p[0].tat - p[0].bt;
	
	avwt = p[0].wt;
	avtat = p[0].tat;
	
	for(i=1;i<n;i++)
	{
 		if(p[i].at<=p[i-1].ct)
 		{
  			p[i].ct=p[i-1].ct+p[i].bt;
 		}

		else
		    p[i].ct=p[i].at+p[i].bt;

		p[i].tat=p[i].ct-p[i].at;
		p[i].wt=p[i].tat-p[i].bt;

		avwt+=p[i].wt;
	avtat+=p[i].tat;
	}
	
	avtat/=n;
	avwt/=n;

	pidSort();

printf("\nFCFS:\n");
display();
}


void main()
{
int z,i;

printf("Enter the number of processes: ");
scanf("%d",&n);

for(i=0;i<n;i++)
{
 p[i].pid=i+1;

 printf("Enter the arrival time of process %d: ",i+1);
 scanf("%d",&p[i].at);

 printf("Enter the burst time of process %d: ",i+1);
 scanf("%d",&p[i].bt);
}

while(1)
{

printf("\nWhat would you like to do? \n1. FCFS \n2. Exit\t");
scanf("%d",&z);

switch(z)
{

case 1: fcfs();
break;

case 2: exit(0);

}

avwt = avtat = 0.0;

for(i=0;i<n;i++)
{
 p[i].tat=0;
 p[i].wt=0;
 p[i].ct=0;
}
}
}