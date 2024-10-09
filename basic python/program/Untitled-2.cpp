#include<iostream>
using namespace std;
class S
{
    public:
    
    
        int a;
        int b;

    
    void call()
    {
        cout<<"enter value in a:";
        cin>>a;
        cout<<"enter value in b:";
        cin>>b;
    }
};
int main()
{
    S s;
    //s.variable();
    s.call();
    cout<<s.a<<" "<<s.b;
    return 0;
}