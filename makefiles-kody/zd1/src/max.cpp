#include <iostream>
#include "./max.h"
using namespace std;
int findBiggestElement(int arr[], int n){
   /* We are assigning the first array element to
    * the temp variable and then we are comparing
    * all the array elements with the temp inside
    * loop and if the element is smaller than temp
    * then the temp value is replaced by that. This
    * way we always have the smallest value in temp.
    * Finally we are returning temp.
    */
   int temp = arr[0];
   for(int i=0; i<n; i++) {
      if(temp<arr[i]) {
         temp=arr[i];
      }
   }
   return temp;
}
int findmax() {
   int n;
   cout<<"Enter the size of array: ";
   cin>>n; int arr[n-1];
   cout<<"Enter array elements: ";
   for(int i=0; i<n; i++){
      cin>>arr[i];
   }
   int biggest = findBiggestElement(arr, n);
   cout<<"Biggest Element is: "<<biggest;
   max();
   return 0;
}
