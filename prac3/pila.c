#include <stdio.h>
void primera(){ 
    printf("En primera\n");
    segunda();
 }
void segunda(){ printf(
    "En segunda\n");
    tercera();
}
void tercera(){ printf(
    "En tercera\n");
    cuarta();
}
void cuarta(){ printf(
    "En cuarta\n");
}
int main(int argc, char *argv[]){
    primera();
    return 0;
}