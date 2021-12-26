#include <iostream>
// Math library in C++
#include <cmath>

using namespace std;

// Function

// int add(int number_One, int number_Two){
//     cout << fmax(number_One, number_Two) << "\n";
//     return number_One + number_Two;
// }
// int main(){
//     string name;
//     cout << add(1, 5) << "\n";
//     cout<< "Enter your name: ";
//     // Easier syntax for input 
//     getline(cin, name);
//     cout << "hello " << name;
//     return 0;
// }

// Getting comfy with syntax

// int main(){
//     string color, pluralNoun, celeb;
//     cout << "Enter a color : ";
//     getline(cin, color);
//     cout << "Enter a plural noun : ";
//     getline(cin, pluralNoun);
//     cout << "Enter a celebrity : ";
//     getline(cin, celeb);

//     cout << "roses are " << color << "\n";
//     cout << pluralNoun << " are blue\n";
//     cout << "I love " << celeb;

//     return 0;
// }

// Working with arrays

// int main(){
//     int array[15];
//     for (int i=0; i<15; i++){
//         array[i] = i+1;
//     }
//     for (int i=0; i<15; i++){
//         cout << array[i] << "\n";
//     }
// }

// Conditons

// int main(){
//     bool isMale = false;
//     bool isTall = false;

//     if (isMale && isTall){
//         printf("%s", "He is a tall person");
//     }
//     else if(!isMale){
//         printf("%s", "You're not male");
//     }
//     else{
//         printf("%s", "You don't match the requirements!");
//     }
// }

// Getting max from two numbers

// int getMax(int num_one, int num_two, int num_three){
//     if (num_one > num_two){
//         if (num_one < num_three){
//             return num_three
//         }
//         return num_one
//     }
//     else{
//         if (num_two < num_three){
//             return num_three;
//         }
//         return num_one;
//  }
// }
// int main(){
//     printf("%d" , getMax(2, 1, 5));
// }

// Memory address and values

// int main(){
//     int age = 18;
//     double gpa = 2.1;
//     string name = "Nikhil";
//     cout << "Name[memory address] : "<< &name << "\nAge[memory address] : "<< &age << "\nGPA[memory address] : " << &gpa << "\n"; 
//     int* pAge = &age;
//     double* pGpa = &gpa;
//     string* pName = &name;
//     cout << "Name : "<< *pName << "\nAge : "<< *pAge << "\nGPA : " << *pGpa; 
// }

// Classes or OOPS

class Book{
private:
    string title;
public:
    string author;
    int pages;
    Book(string atitle, string aauthor, int apages){
        title = atitle;
        author = aauthor;
        setPages(apages); 
    }
    // Setters
    void setPages(int apages){
        if (apages > 100){
            pages = apages;
        }
        else{
            pages=0;
        }
    }

    bool isBig(){
        if (pages > 100){
            return 1;
        }
        return 0;
    }
};

int main(){
    Book book1("TMNT", "no idea", 105);
    cout << book1.isBig();
}

// Notes to self:

// Strings are mutable in C++.

// "and" and "or" operators use the primitive symbols.
//   &&       ||

// "a" is added in the constructor for the denoting it's an arg.