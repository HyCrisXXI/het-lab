#include <stdio.h>

void cuarta(){ 
    printf("En cuarta\n");
}

void tercera(){ 
    printf("En tercera\n");
    cuarta();
}

void segunda(){ 
    printf("En segunda\n");
    tercera();
}

void primera(){ 
    printf("En primera\n");
    segunda();
}

int main(int argc, char *argv[]){
    primera();
    return 0;
}