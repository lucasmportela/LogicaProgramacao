#include <stdio.h>
#include <string.h>
int main(void) {
    
    char operacao[20];
    int num1, num2, result = 0;
    
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);
    
    printf("Digite o segundo número: ");
    scanf("%d", &num2);
    
    printf("Digite a operacao (soma | subtracao | divisao | multiplicacao): ");
    scanf("%s", operacao);  
    
    if (strcmp(operacao, "soma") == 0) {
        result = num1 + num2;
        
    } else if (strcmp(operacao, "subtracao") == 0) {
        result = num1 - num2;
        
    } else if (strcmp(operacao, "divisao") == 0) {
        result = num1 / num2;
        
    } else if (strcmp(operacao, "multiplicacao") == 0) {
        result = num1 * num2;
    }
    
    printf("Resultado da operacao: %d\n", result);
    return 0;
}