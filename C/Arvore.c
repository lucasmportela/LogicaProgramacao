#include <stdio.h>
#include <stdlib.h>

struct item 
{
    int cod;
};

typedef struct item Item;

struct node 
{
    Item item;
    struct node *left;
    struct node *right;
};

typedef struct node Node;

Node *iniciar()
{
    return NULL;
}

Item itemCriar(int cod)
{
    Item item;
    item.cod = cod;
    return item;
}

Node *inserir(Node *raiz, Item x)
{
    if(raiz == NULL)
    {
        Node *aux = (Node *)malloc(sizeof(Node));
        aux->item = x;
        aux->left = NULL;
        aux->right = NULL;
        return aux;
    } 
    else
    {
        if(x.cod > raiz->item.cod)
        {
            raiz->right = inserir(raiz->right, x);
        }
        else if (x.cod < raiz->item.cod)
        {
            raiz->left = inserir(raiz->left, x);
        }
    }
    return raiz;
}

void arvorePrint(Node *raiz)
{
    if (raiz != NULL)
    {
        printf("%d ", raiz->item.cod);
        arvorePrint(raiz->left);
        arvorePrint(raiz->right);
    }
}

void arvoreFree(Node *raiz)
{
    if(raiz != NULL)
    {
        arvoreFree(raiz->left);
        arvoreFree(raiz->right);
        free(raiz);
    }
}

int main()
{
    Node *raiz = iniciar();
    raiz = inserir(raiz, itemCriar(10));
    raiz = inserir(raiz, itemCriar(15));
    raiz = inserir(raiz, itemCriar(20));
    raiz = inserir(raiz, itemCriar(12));
    raiz = inserir(raiz, itemCriar(5));
    arvorePrint(raiz);

    printf("\n");
    arvoreFree(raiz);
    return 0;
}