#include<stdio.h>
int main()
{
    int pass, i;
    for(i=1; i<=3; i++)
    {
        printf("Enter Password (chance %d/3): ", i);
        scanf("%d", &pass);
        if(pass == 1234)
        {
            printf("\n\tWelcome Ghost!\n");
            return 0;
        }
        else
        {
            printf("\n\tWrong number\n");
        }
    }
    printf("\n\t3 bar galat! System Locked\n");
    return 0;
}
