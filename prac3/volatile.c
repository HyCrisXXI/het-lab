#include <stdio.h>

volatile int la_global = 1;

int main() {
	volatile int la_local = 2;
	int i = 0;
	while(i < 10) {
		i++;
	}
	// printf("%d", i); // para que el compilador no elimine el bucle
	return 0;
}
