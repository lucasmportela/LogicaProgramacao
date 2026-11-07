#include <stdio.h>

char name[30], sex[2];

int main(void){

    printf("Informe seu nome:");
    scanf("%s", &name);

    printf("Informe seu sexo:");
    scanf("%s", &sex);

    if (sex == 'm'){
        printf("Ilmo Sr. %s", name);
    }
    else if (sex == "f"){
        printf("Ilma Sra. %s", name);
    }
    else{
        printf("e duro %s", sex);
    }
}