#include <stdio.h>
#include <stdlib.h>


int main()
{
    string Name, Sex;
    
    printf("\nInforme seu nome e sexo:");
    scanf("%c, %c", &Name, &Sex);
    if(Sex == "masculino")
    {
        printf("\n Ilmo Sr. \n %c", Name);
    }
    if(Sex == "feminino")
    {
        printf("\n Ilma Sra. \n %c", Name);
    }
    return 0;
}