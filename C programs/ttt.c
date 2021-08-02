#include <iostream>
using namespace std;
int main(){
    int n,flag;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int temp=-9999;
    for(int i=0;i<n;i++){
        if(temp<=a[i]){
            temp=a[i];
        }else if(temp>a[i]){
            flag=1;
            break;
        }
    }
if(flag==1){
    cout<<"NON MONOTONOUS";
}
else{
    cout<<"MONOTONOUS";
}
}

