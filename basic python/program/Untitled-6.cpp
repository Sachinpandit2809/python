#include<iostream>
using namespace std;
class A
{
    public:
    int x,y;
    A(int a,int b)
    {
        x=a;
        y=b;
    }
    A(A&i)
    {
        x=i.x;
        y=i.y;

    }
};
int main()
{
    A a1(20,10);
    A a2(a1);
    cout<<a2.x<<"\n";
    cout<<a2.y;
    return 0;
}