#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


void generateData()
{
	FILE *fptr;
	int numOfCandidates, numOfVoters;
	int preference[numOfVoters][numOfCandidates];
	fptr = fopen("data.txt", "w+");

	if (fptr == NULL)
	{
		printf("Error!! opening file");
		exit(1);
	}

	printf("Enter the number of candidates: ");
	scanf("%d", &numOfCandidates);
	fprintf(fptr,"%d ", numOfCandidates);
	printf("Enter the number of voters: ");
	scanf("%d", &numOfVoters);
	fprintf(fptr,"%d", numOfVoters);
	//fprintf(fptr,"\n");


	
	
	for (int i = 0; i < numOfVoters; ++i)
    {
        for (int j = 0; j < numOfCandidates; ++j)
        {

            preference[i][j] = rand()%numOfCandidates + 1;
            fprintf(fptr,"%d ", preference[i][j]);
        }
        fprintf(fptr,"\n");
    }
	 
	

	fclose(fptr);
	
}

void readFile()
{
	FILE *f = fopen("data.txt", "r");
}
int main()
{
    generateData();
    return 0;
}
