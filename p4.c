#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main(void)
{
	long int i,n;
	double x,y;
	n=10000;
	FILE*fp;
	fp=fopen("data.txt","w");
	for(i=0;i<=n;i++)
	{
		x=(double)rand()/(double)RAND_MAX;
		y=-0.5*log(x);
		fprintf(fp,"%lf\n",y);
	}
	fclose(fp);
	system("python histogram.py");
	return 0;
}

