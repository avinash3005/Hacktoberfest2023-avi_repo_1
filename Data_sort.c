#include <stdio.h>

struct employees
{
    int id;
    char name[80];
    int ddate;
    int mdate;
    int ydate;
    int salary;
}data[100];

void accept(struct employees list[], int s);
void display(struct employees list[], int s);
void bsortDesc(struct employees list[], int s);

int main()
{
    int n;

    printf("Number of records you want to enter? : ");
    scanf("%d", &n);

    accept(data, n);
    printf("\nBefore sorting");
    display(data, n);
    bsortDesc(data, n);
    printf("\nAfter sorting");
    display(data, n);

    return 0;
} 

void accept(struct employees list[80], int s)
{
    int i;
    for (i = 0; i < s; i++)
    {
        printf("\n\nEnter data for Record #%d", i + 1);
        
        printf("\nEnter id : ");
        scanf("%d", &list[i].id);

        printf("Enter name : ");
        scanf("%s", &list[i].name);

        printf("Enter joining date: ");
        scanf("%d%d%d", &list[i].ddate, &list[i].mdate, &list[i].ydate);

        printf("Enter salary : ");
        scanf("%d", &list[i].salary);
    } 
}

void display(struct employees list[80], int s)
{
    int i;
    
    printf("\n\nID\tName\tJoining_Date\tSalary\n");
    for (i = 0; i < s; i++)
    {
        printf("%d\t %s\t\t %d/%d/%d\t\t %d\n", list[i].id, list[i].name, list[i].ddate, list[i].mdate, list[i].ydate, list[i].salary);
    } 
}

void bsortDesc(struct employees list[80], int s)
{
    int i, j;
    struct employees temp;
    
    for (i = 0; i < s - 1; i++)
    {
        for (j = 0; j < (s - 1-i); j++)
        {
            if (list[j].salary < list[j + 1].salary)
            {
                temp = list[j];
                list[j] = list[j + 1];
                list[j + 1] = temp;
            } 
        }
    }
}
