#include<stdio.h>

void main(){

              int bsize[10],psize[10],flag[10],allocation[10],bno,pno,i,j;
		int  swap;

              for(i=0;i<10;i++){

                           flag[i]=0;

                           allocation[i]=-1;

              }

              printf("Enter the no of blocks: ");

              scanf("%d",&bno);

             

              printf("\nEnter the size of each block:\n");

              if(bno>10){

                           printf("Maximum no of blocks should be 10");

              }

              else{

                           for(i=0;i<bno;i++){

                                         scanf("%d",&bsize[i]);

                           }

              }

	      
for(i = 0 ; i < bno - 1; i++)
{
for(j = 0 ; j < bno-i-1; j++)
{
if(bsize[j] > bsize[j+1]) 
{
swap=bsize[j];
bsize[j]=bsize[j+1];
bsize[j+1]=swap;
}
}
} 

            

              printf("\nEnter the no of processes: ");

              scanf("%d",&pno);

             

              printf("\nEnter the size of each process:\n");

              if(pno>10){

                           printf("Maximum no of processes should be 10");

              }

              else{

                           for(i=0;i<pno;i++){

                                         scanf("%d",&psize[i]);

                           }

              }

              for(i=0;i<pno;i++){

                           for(j=0;j<bno;j++){

                                         if(flag[j]==0 && bsize[j]>=psize[i]){

                                                       flag[j]=1;

                                                       allocation[j]=i;

                                                       break;

                                         }

                           }

              }

 

              printf("\nBlock no\tSize\t\tProcess no\tSize");

              for(i=0;i<bno;i++){

                           printf("\n%d\t\t%d\t\t",i+1,bsize[i]);

                           if(flag[i]==1){

                                         printf("%d\t\t%d",allocation[i]+1,psize[allocation[i]]);

                           }

                           else{

                                         printf("Not allocated");

                           }

              }

}
