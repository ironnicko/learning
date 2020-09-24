#include <stdio.h>
#include <stdlib.h>

/*int main()
{
    int o1;
    printf("Enter Your No.");
    int o2;
    scanf("%d",&o2);
    printf("Enter Your No.");
    scanf("%d",&o1);
    add(o1,o2);


    return 0;
}

void add(int n,int f){

    printf("%d",n+f);

    }
/* scanf example */
/*


int main ()
{
  char str [80];
  int i;

  printf ("Enter your family name: ");
  scanf ("%9s",str);
  printf ("Enter your age: ");
  scanf ("%d",&i);
  printf ("Mr. %s , %d years old.\n",str,i);
  printf ("Enter a hexadecimal number: ");
  scanf ("%x",&i);
  printf ("You have entered %#x (%d).\n",i,i);

  return 0;
}

double cube(double num);

int main(){
    float no;
    printf("Enter the no.\n");
    scanf("%f",&no);
    printf("Cube of %f %f",no,cube(no));
    return 0;
}

double cube(double num){
    double result = num*num*num;
    return result;

}


int max(int num, int num1, int num2){
    int result;
    int g;
    if(num>=num1  && num >= num2){
            result=num;
}   else if(num1>=num && num1>=num2){
        result=num1;

}   else{
    result = num2;
}
    return result;

}

int main(){
    int n;
    int j;
    int a;
    printf("Enter No.:");
    scanf("%d",&n);
    printf("Enter No.:");
    scanf("%d",&j);
    printf("Enter No.:");
    scanf("%d",&a);
    printf("Larger no: %d",max(n,j,a));
    if(2>3||8>9){
        printf("Yep");
}   else{
    printf("\nNope");
}
    return 0;
}

 ! == not in py

  Calc

int main(){
    double n;
    double a;
    char p;
    printf("NO:\n");
    scanf("%lf",&n);
    printf("NO:\n");
    scanf("%lf",&a);
    printf("Enter the operation symbol:\n");
    scanf(" %c",&p);

    if(p=="+"){
        printf("%f",a+n);
}   else if(p=="-"){
        printf("%f",a-n);

}   else if(p=="*"){
        printf("%f",a*n);

}   else{
    printf("Wrong O");
}
    return 0;
 }

*/
/*
int main(){
    char grade;
    scanf(" %c",&grade);
    switch(grade){
    case 'A':
        printf("you did great");
        break;
    case 'B':
        printf("you did okay");
        break;
    case 'F':
        printf("you Failed");
        break;
    default:
        printf("Invalid Grade");
    }

}
*

struct people{
    char name[100];
    char grade[3];
    int age;

};

int main(){

    struct people p1;
    strcpy(p1.name,"Nikhil");
    strcpy(p1.grade,"XII");
    p1.age = 17;

    printf("%s", p1.name);

}
*

int main(){
    int index = -5;
    do {
        printf("%d\n",index*index);
        index++;
}   while(index<=0);


    return 0;
}

*/

/* While loop */

/*
int main(){
    int index = 1;
    while(index <= 5){
        if(index==1){
            printf("First Loop\n");
    }   else if(index==2){
            printf("Second Loop\n");
    }   else if(index==3){
            printf("Third Loop\n");
    }   else if(index==4){
            printf("Fourth Loop\n");
    }   else{
            printf("Last\n");
        }
        index++;
    }


    return 0;
}

int guess();

int main(){
    guess();
}


int guess(){
    int secret_no = 5;
    int guess;
    int guess_count = 0;
    int guess_limit = 3;
    int outofg = 0;

    while(guess != secret_no && outofg == 0){
        if(guess_count < guess_limit){
            printf("Enter a NO.\n");
            scanf("%d",&guess);
            guess_count++;
        } else {
            outofg = 1;
        }
    }
    if (outofg == 1){
        printf("Outta guesses");
}   else{
        printf("you win!");
}
}


int main(){
    int no[] = {4,4,54,4,54,5,2,5};
    int i;
    for(i=0; i<8; i++){
    printf("%d\n",no[i]);
    }
    return 0;
}


int main(){
    int nums[3][2] = {
        {1,2},
        {3,4},
        {5,6}
        };
    int i,j;
    for(i=0;i<3;i++){
        for(j=0;j<2;j++){
            printf("%d,",nums[i][j]);
        }
        printf("\n");
    }
    return 0;
}

int main(){
    int age = 30;
    int * pAge = &age;
    double gpa = 3.4;
    char grade = 'A';
    double *pGpa = &gpa;
    char *pGrade = &grade;

    printf("age: %d\ngrade: %lf\ngpa: %c",*pAge,*pGrade,*pGpa);


    return 0;
}


int main(){
    char line[255];
    FILE * fpointer = fopen("wordbank.txt","r");
    fgets(line, 255, fpointer);
    printf("%s",line);
    fclose(fpointer);
    return 0;
}
*/

/*

double cube(double num);

int main(){
    float no;
    printf("Enter the no.\n");
    scanf("%f",&no);
    printf("Cube of %f is %f",no,cube(no));
    return 0;
}

double cube(double num){
    double result = num*num*num;
    return result;

}


int main(){
    int n=10, j=20;
    op(n,j);

    return 0;
}

void op(int n, int j){
    printf("%d",n*j);

}
*/
struct people{
    char name[100];
    char grade[3];
    int age;

};

int main(){

    struct people p1;
    strcpy(p1.name,"Nikhil");
    strcpy(p1.grade,"XII");
    p1.age = 17;

    struct people p2;
    strcpy(p2.name,"Bezoz");
    strcpy(p2.grade,"XII");
    p2.age = 17;


    printf("%s\n", p1.name);
    printf("%s",p2.name);
}
