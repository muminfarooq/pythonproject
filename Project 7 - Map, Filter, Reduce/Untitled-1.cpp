#include <iostream>
class Car{
 float price;
 public:
 void acceptprice(){
     cout <<"Enter Price :";
     cin>> price

 }
 void honk()
 {
     cout <<endl <<"BEEP BEEP !"
 }
};
int main(){
    Car ford;
    ford.acceptprice();
    ford.honk();
    return 0;
}