#include<iostream>
using namespace std;
class A
{
    public:
    int x,y;
    int e;
    float d;
    char f;
    A(int a,int b)
    {
        x=a;
        y=b;
    }
    A(float p,int q,char r)
    {
        d=p;
        e=q;
        f=r;

    }
};
int main()
{
    A a(1,2);
    cout<<a.x<<" "<<a.y;
    cout<<"\n";
    A z(2.3,4,'x');
    cout<<z.d<<"\t"<<z.e<<"\t"<<z.f;
    return 0;
}