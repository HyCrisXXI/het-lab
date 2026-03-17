#include <stdio.h>

int main(int argc, char **argv) {
    if(argc < 2) {
        printf("Uso: e3.c <num1> [<numn>]");
        return -1;
    }

    for(int i = 1; i < argc; i++) {
        printf("Numero %d: %s\n", i, argv[i]);
    }

    return 0;
}