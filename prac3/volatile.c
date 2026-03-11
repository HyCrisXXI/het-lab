#include <stdio.h>

volatile int la_global;

int main() {
	volatile int la_local;
	printf("Variable global direccion: %p\n", &la_global);
	printf("Variable local direccion: %p\n", &la_local);
	return 0;
}
