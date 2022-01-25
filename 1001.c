#include <stdio.h>

int main()
{
    int n = 0, count = 0;
    scanf("%d", &n);
    while (n != 1)
    {
        if (n % 2 == 0)
        {
            // even number
            n /= 2;
        }
        else
        {
            //odd number
            n = (3*n+1)/2;
        }
        count++;
    }
    printf("%d\n", count);
    return 0;
}