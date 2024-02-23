/*#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char word[100];
    printf("Enter a word/phrase: ");
    scanf("%s", &word);
    char reversed[100];
    int n = strlen(word);
    int i = 0;
    while(i < n) {
        reversed[i] = word[n - i - 1];
        i++;
    }
    reversed[i] = '\0';
    printf("%s", reversed);    
}
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a;
    int b;
    printf("Enter a rectangle width: ");
    scanf("%d", &a);
    printf("Enter a rectangle height: ");
    scanf("%d", &b);
    int perimeter = 2 * (a + b);
    int area = a * b;
    printf("Perimeter of this rectangle is equal to %d\n", perimeter);
    printf("Area of this rectangle is equal to %d", area);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    double r;
    double pi = 3.1415926;
    printf("Enter a radius of a circle: ");
    scanf("%lf", &r);
    double perimeter = 2 * pi * r;
    double area = pi * (r * r);
    printf("Perimeter of this circle is equal to %lf\n", perimeter);
    printf("Area of this circle is equal to %lf", area);
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int arabic;
    printf("Enter a number from 1 to 10: ");
    scanf("%d", &arabic);
    switch(arabic) {
        case 1:
            printf("I");
            break;
        case 2:
            printf("II");
            break;
        case 3:
            printf("III");
            break;
        case 4:
            printf("IV");
            break;
        case 5:
            printf("V");
            break;
        case 6:
            printf("VI");
            break;
        case 7:
            printf("VII");
            break;
        case 8:
            printf("VIII");
            break;
        case 9:
            printf("IX");
            break;
        case 10:
            printf("X");
            break;
        default:
            printf("Error! Wrong number!");
    }
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a;
    printf("Please input a number ");
    scanf("%d", &a);
    while(a < 10) {
        a++;
        printf("%d\n", a);
    };
    printf("Now a is equal to 10 or higher than 10!");
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char card_name[3];
    int score = 0;
    while(card_name[0] != 'X'){
        printf("Enter card value: ");
        scanf("%2s", card_name);
        int val = 0;
        switch (card_name[0])
        {
        case 'K':
        case 'Q':
        case 'J':
            val = 10;
            break;
        case 'A':
            val = 11;
            break;
        case 'X':
            continue;
        default:
            val = atoi(card_name);
            if((val < 1) || (val > 10)){
                printf("Error");
                continue;
            }
        }
        if((val > 2) && (val < 7)){
            score++;
        } else if(val == 10){
            score--;
        }
        printf("Score now is: %i\n", score);
    }
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    printf("Enter number of days: ");
    scanf("%d", &x);
    int years = x / 365;
    int weeks = (x % 365) / 7;
    int days = (x % 365) % 7;
    if (years > 10) {
        printf("More than a decade!\n");
    } else if (years > 100) {
        printf("More than a century!\n");
    }
    printf("Years: %d\n", years);
    printf("Weeks: %d\n", weeks);
    printf("Days: %d\n", days);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

void main() //You can set main() type to void and it'll still work!!!
{
    int id;
    int hours;
    int salary;
    printf("Enter employee ID: ");
    scanf("%d", &id);
    printf("Enter number of working hours: ");
    scanf("%d", &hours);
    printf("Enter salary (USD/hrs): ");
    scanf("%d", &salary);
    int money = salary * hours;
    printf("Employee's ID is %d\n", id);
    printf("Employees total salary is %d USD", money);
}

#include <stdio.h>
#include <stdlib.h>

void main(){
    int x1;
    int x2;
    int x3;
    int max;
    printf("Enter first value: ");
    scanf("%d", &x1);
    printf("Enter second value: ");
    scanf("%d", &x2);
    printf("Enter third value: ");
    scanf("%d", &x3);
    if(x1 < x2){
        max = x2;
    } else {
        max = x1;
    }
    if(max < x3) {
        max = x3;
    }
    printf("%d", max);
} */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main(){
    int x1;
    int x2;
    int y1;
    int y2;
    printf("Enter x1 value: ");
    scanf("%d", &x1);
    printf("Enter x2 value: ");
    scanf("%d", &x2);
    printf("Enter y1 value: ");
    scanf("%d", &y1);
    printf("Enter y2 value: ");
    scanf("%d", &y2);
    int xlen = x2 - x1;
    int ylen = y2 - y1;
    float FullLen = sqrt(xlen * xlen + ylen * ylen);
    printf("%f", FullLen);
}