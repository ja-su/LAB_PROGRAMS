#include<stdio.h>
#include<stdlib.h>

struct process
{
 int pid;
 int at;
 int wt;
 int tat;
 int bt;
 int priority;
 int ct;
 int pos;
 int rt;
}p[20],temp;

int n,tq;
float avwt,avtat;

void display()
{
 int i;
 printf("Process ID\tArrival Time\tBurst Time\tWaiting Time\t\tTurnaround Time\n");
 for(i = 0; i < n; i++)	printf("%d\t\t%d\t\t%d\t\t%d\t\t\t%d\n", p[i].pid, p[i].at, p[i].bt, p[i].wt, p[i].tat);
 printf("\nAverage Waiting Time: %f", avwt);
 printf("\nAverage Turnaround Time: %f\n", avtat);
}

void swap(int i, int j)
{
 temp=p[i];
 p[i]=p[j];
 p[j]=temp;
}

void atSort()
{
 int i,j;
 for(i=0;i<n-1;i++)
 {
  for(j=0;j<n-i-1;j++)
  {
   if(p[j].at>p[j+1].at)	
   swap(j,j+1);
  }
 }
}

void pidSort()
{
 int i,j;
 for(i=0;i<n-1;i++)
 {
  for(j=0;j<n-i-1;j++)
  {
   if(p[j].pid>p[j+1].pid)	
   swap(j,j+1);
  }
 }
}

int fin()
{
 int i;
 for(i = 0; i < n; i++)
 {
  if(p[i].rt != 0)
  return 0;
 }
 return 1;
}


void rr()
{
 int i, small, c = 0, first, clk = 0, position = 1;
 printf("\nEnter time quantum: ");
 scanf("%d", &tq);
 for(i = 0; i < n; i++)
   p[i].rt = p[i].bt;
 atSort();
 while(fin() == 0)
 {
  for(i = 0; i < n; i++)
  {
   if(p[i].at == clk)
   p[i].pos = position++;
  }
  if(c == tq)
  {
   c = 0;
   p[first].pos = position++;
  }
  for(i = 0, small = 100; i < n; i++)
  {
   if(p[i].pos < small && p[i].pos != 0 && p[i].rt != 0)
   {
    first = i;
    small = p[i].pos;
   }
  }
  clk++;
  p[first].rt--;
  c++;
  if(p[first].rt == 0)
  {
   c = 0;
   p[first].pos = 0;
   p[first].ct = clk;
   p[first].tat = p[first].ct - p[first].at;
   p[first].wt = p[first].tat - p[first].bt;
   avtat += p[first].tat;
   avwt += p[first].wt;
  }
}

  avtat /= n;
  avwt /= n;

  pidSort();
  printf("\nRound Robin:\n");
  display();
}

void priorSort()
{
 int i,j;
 for(i=0;i<n-1;i++)
 {
  for(j=0;j<n-i-1;j++)
  {
   if(p[j].priority>p[j+1].priority)    
   swap(j,j+1);
  }
 }
}

void prior()
{
 int i, j, pct, highest, loc, f, flag = 0;
 for(i = 0; i < n; i++)
 {
  if(p[i].at > 0)
  flag = 1;
 }

 if(flag == 1)
  atSort();
 else
  priorSort();

 p[0].ct = p[0].at+ p[0].bt;
 p[0].tat = p[0].ct - p[0].at;
 p[0].wt = p[0].tat - p[0].bt;

 avtat= p[0].tat;
 avwt= p[0].wt;

 for(i = 1; i < n; i++)
 {
  pct = p[i - 1].ct;
  highest = 20;
  f = 0;

 for(j = i; j < n; j++)
 {
  if(p[j].at <= pct && p[j].priority < highest)
  {
   f = 1;
   loc = j;
   highest = p[j].priority;
  }

  if(f == 0)
  {
   if(p[j].at >= pct && p[j].priority < highest)
   {
    loc = j;
    highest=p[j].priority;
   }
 }
}

 if(f == 1)
  p[loc].ct= pct + p[loc].bt;
 else
  p[loc].ct = p[loc].at + p[loc].bt;

 p[loc].tat = p[loc].ct - p[loc].at;
 p[loc].wt = p[loc].tat - p[loc].bt;

 swap(loc, i);

 avtat+= p[i].tat;
 avwt+= p[i].wt;
}

 avtat /= n;
 avwt /= n;

 pidSort();
 printf("\nPriority Scheduling:\n");
 display();
}

void main()
{
 int z,i;
 while(1)
 {
  printf("\nWhat would you like to do? \n1. Round Robin \n2. Priority Scheduling \n3. Exit\n");
  printf("Enter your choice: ");
  scanf("%d",&z);
  switch(z)
  {
   case 1: printf("Enter the number of processes: ");
           scanf("%d",&n);
           for(i=0;i<n;i++)
           {
            p[i].pid=i+1;
            printf("Enter the arrival time of process %d: ",i+1);
            scanf("%d",&p[i].at);
            printf("Enter the burst time of process %d: ",i+1);
            scanf("%d",&p[i].bt);
           }
           rr();
           break;
   case 2: printf("Enter the number of processes: ");
           scanf("%d",&n);
           for(i=0;i<n;i++)
           {
            p[i].pid=i+1;
            printf("Enter the arrival time of process %d: ",i+1);
            scanf("%d",&p[i].at);
            printf("Enter the burst time of process %d: ",i+1);
            scanf("%d",&p[i].bt);
            printf("Enter the priority of process %d: ",i+1);
            scanf("%d",&p[i].priority);
           }
           prior();
           break;
   case 3: exit(0);
  }
  avwt=avtat=0.0;
  for(i=0;i<n;i++)
  {
    p[i].tat=0;
    p[i].wt=0;
    p[i].ct=0;
    p[i].pos=0;
    p[i].rt=p[i].bt;
  }
 }
}