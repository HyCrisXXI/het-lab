#include <stdio.h>

void funct(int a, int b, int c, int d, int e, int f, int g){
    printf("%d", a);
    printf("%d", b);
    printf("%d", c);
    printf("%d", d);
    printf("%d", e);
    printf("%d", f);
    printf("%d", g);
}

int main(int argc, char *argv[]){
    funct(1,2,3,4,5,6,7);
    return 0;
}