# practice
Working on my assignments in c
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define MAT_SIZE 9
int main()
{
	int A[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
	int x[3];
	int y[3] = {2,1,3};
	int i,j;
	
	
	//printing the matrix
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d ", A[i][j]);
		}
		printf("\n");
	}
	
	#pragma omp parallel default(none) shared(i,x,y,A) private(j)
	{
		int localResult[3] = {};
		int i,j;		
		
		for (i = 0; i < 3; ++i)
		{			
			#pragma omp parallel for schedule(dynamic)
			for (j = 0; j < 3; j++)
			{
				localResult[i] += A[i][j]*y[j];
			}			
		}
		#pragma omp critical
		{
			for (i = 0; i < 3; i++)
				x[i] += localResult[i];
		}
		for (i = 0; i < 3; i++)
			printf("Result[%d] = %d\n ", i, x[i]);
		
				
		
	}
}
