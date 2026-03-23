#include <stdio.h>

int main() {
    int tabla[5]; 
    int i;

    for(i = 0; i < 5; i++) {
        tabla[i] = i * 10;
        printf("direccion de tabla[%d] : %p\n", i, &tabla[i]);
    }

    return 0;
}