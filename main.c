#include <stdio.h>

/*count digits\white space\others */
int main(){
	int c, i, nwhite, others;
	int ndigits[10];

	nwhite = others = 0;

	for (i = 1; i < 10; i++){
		ndigits[i] = 0;
	}

	while((c = getchar()) != EOF){
		if (c >= '0' && c <= '9'){
			ndigits[c-'0']++;
		}
		else if (c == ' ' || c == '\n' || c == '\t')
		{
			/* code */
			nwhite++;
		}
		else{
			others++;
		}
	}
	printf("digits =");
	for (i = 0; i < 10; i++){
		printf(" %d", ndigits[i]);
	}
	printf(", white space = %d, other = %d\n", nwhite, others);

}