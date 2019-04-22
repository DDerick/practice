#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


void generateData()
{
	FILE *fptr;
	int pref, temp;
	int numOfCandidates, numOfVoters;
	int c ;
	int randomVoters[numOfCandidates];
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
	fprintf(fptr,"\n");	
	
	srand(time(NULL));
	for (int i = 0; i < numOfCandidates + 1; i++)
	{
		randomVoters[i] = i +1;
	}
	for (int i = 0; i < numOfCandidates; i++)
	{
		pref = rand()%numOfCandidates + 1;
		temp = randomVoters[i];
		randomVoters[i] = randomVoters[pref];
		randomVoters[pref] = temp;
	}

	
	for (int i = 0; i < numOfVoters; ++i)
    {
		for (int j = 0; j < numOfCandidates; ++j)
        {

            preference[i][j] = randomVoters[i];
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
