#include <stdio.h>
void main()
{
    int alloc[50][50],max[50][50],avail[3],n,m,i,j;
    char ch;
    //n = number of processes
    //m = number of resources
    printf("Enter  number of processes: ");
    scanf("%d",&n);
    printf("Enter number of resources: ");
    scanf("%d",&m);

    //allocation
    printf("!-- Enter allocation matrix --!\n");
    for(i = 0;i < n;i ++)
    {
        ch = 'A';
        for(j = 0;j < m;j ++)
        {
            printf("Enter %d process for %c resource:  ",i+1,ch);
            scanf("%d",&alloc[i][j]);
            ch ++;
        }
    }

    printf("!--Enter max matrix--!\n");
    for(i = 0;i < n;i ++)
    {
        ch = 'A';
        for(j = 0;j < m;j ++)
        {
            printf("Enter %d process for %c resource:  ",i+1,ch);
            scanf("%d",&max[i][j]);
            ch ++;
        }
    }

    printf("!--Enter available matrix--!\n");
    ch = 'A';
    for(i = 0;i < m;i ++)
    {
        printf("At %c resource:  ",ch);
        scanf("%d",&avail[i]);
        ch ++;
    }

    
		int f[n], ans[n], ind = 0,k;
	for (k = 0; k < n; k++) {
		f[k] = 0;
	}
	int need[n][m];
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++)
			need[i][j] = max[i][j] - alloc[i][j];
	}
	int y = 0;
	for (k = 0; k < n; k++) {
		for (i = 0; i < n; i++) {
			if (f[i] == 0) {

				int flag = 0;
				for (j = 0; j < m; j++) {
					if (need[i][j] > avail[j]){
						flag = 1;
						break;
					}
				}

				if (flag == 0) {
					ans[ind++] = i;
					for (y = 0; y < m; y++)
						avail[y] += alloc[i][y];
					f[i] = 1;
				}
			}
		}
	}

	int flag = 1;

	for(int i=0;i<n;i++)
	{
	if(f[i]==0)
	{
		flag=0;
		printf("The following system is not safe");
		break;
	}
	}

	if(flag==1)
	{
	printf("Following is the SAFE Sequence\n");
	for (i = 0; i < n - 1; i++)
		printf(" P%d ->", ans[i]);
	printf(" P%d", ans[n - 1]);
	}




	
}