#include <stdio.h>

int main(int argc, const char * argv[])
{
	printf("%d\n",argc);
	for (int i=0; i<argc; i++){
		printf("var %d: %s\n", i,argv[i]);
	}
	return 0;
}
