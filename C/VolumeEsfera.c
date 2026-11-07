#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

float raio, volume;

int main(){
    printf("Informe o raio:");
    scanf("%f", &raio);
    volume= (4.0/3.0)*M_PI*pow(raio,3);
    printf("%f", volume);
}