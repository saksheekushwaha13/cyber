#include<iostream>
#include<string.h>
using namespace std;



int main() {

  string str;
  cin>>str;
  for(int i=0;i<str.length();i++)
  {
    int j = int(str[i]) ;
    if(j>= 97 && j<= 122)
    {
        int m = j - 96;
       if(i == 0)
       {
           for(int k=1 ;k<=m;k++)
           {
               cout<<"#";
           }
       }else if(i%2 == 0)
       {
        for(int k=1 ;k<=m;k++)
           {
               cout<<"#";
           }   
       }else{
           for(int k=1 ;k<=m;k++)
           {
               cout<<"$";
           } 

       }
    }else{
                int m = j - 64;
                  if(i == 0)
       {
           for(int k=1 ;k<=m;k++)
           {
               cout<<"#";
           }
       }else if(i%2 == 0)
       {
        for(int k=1 ;k<=m;k++)
           {
               cout<<"#";
           }   
       }else{
           for(int k=1 ;k<=m;k++)
           {
               cout<<"$";
           } 

       }

    }
  }
	return 0;
}
//97 and 122