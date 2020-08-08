#include <iostream>
using namespace std;

int f1(int n){
    int a = 0;
    if (n <= 0){
        cout<< "You've not entered a natural number." << endl;
    }
    else{
        for(int i = 1;i <= n; i++){
            a = a + i;
        }
        cout<< "The sum of natural numbers from 1 to n is " << a << endl;
    }
    return a;
}

double f2(int n){
    double p = 1;
    if (n <= 0){
        cout<< "You've not entered a natural number." << endl;
    }
    else{
        for(int i = 1;i <= n; i++){
            p = p*i;
        }
        cout<< "The product of natural numbers from 1 to n is " << p << endl;
    }
    return p;
}

float f3(){
    int r = 1;
    float a = 0;
    int s = 1/r;
    cout << s<< endl;

    while(1.0/r >= 0.001){
        a = a + 1.0/r;
        r = r+1;
        //cout<< r <<endl;
    }
    //cout << r << endl;
    cout<< "The sum of harmonic progression of natural numbers is"<< a << "(till 1001 terms)."<< endl;
    return a;
}

int main(){
    int n,r;
    cout << "Please enter any integer:" ;
    cin>> n;
    f1(n);
    cout << "Please enter any integer,again:" ;
    cin>> r;
    f2(r);
    f3();
    return 0;
}
