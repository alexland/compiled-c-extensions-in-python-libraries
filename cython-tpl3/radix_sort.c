#include <stdio.h>
#define MAX 20
#define SHOWPASS
#define BASE 10
void print(int *a, int n)
{
  int i;
  for (i = 0; i < n; i++)
    printf("%d\t", a[i]);
}
 
void radixsort(int *a, int n)
{
  int i, b[MAX], m = a[0], exp = 1;
 
  // get the greatest value in the array a and assign it to m
  for (i = 1; i < n; i++)
  {
    if (a[i] > m)
      m = a[i];
  }
 
  // loop until exp is bigger than the largest number
  while (m / exp > 0)
  {
    int bucket[BASE] = { 0 };
 
    // count the number of keys that will go into each bucket
    for (i = 0; i < n; i++)
      bucket[(a[i] / exp) % BASE]++;
 
    // add the count of the previous buckets to acquire the indexes after the end of each bucket location in the array
    for (i = 1; i < BASE; i++)
      bucket[i] += bucket[i - 1]; //similar to count sort algorithm i.e. c[i]=c[i]+c[i-1];
 
    // starting at the end of the list, get the index corresponding to the a[i]'s key, decrement it, and use it to place a[i] into array b.
    for (i = n - 1; i >= 0; i--)
      b[--bucket[(a[i] / exp) % BASE]] = a[i];
 
    //Copy array b to array a
    for (i = 0; i < n; i++)
      a[i] = b[i];
 
    // multiply exp by the BASE to get the next group of keys
    exp *= BASE;
 
    #ifdef SHOWPASS
      printf("\nPASS   : ");
      print(a, n);
    #endif
  }
}
 
int main()
{
  int arr[MAX];
  int i, n;
  printf("Enter total elements (n <= %d) : ", MAX);
  scanf("%d", &n);
  n = n < MAX ? n : MAX;
 
  printf("Enter %d Elements : ", n);
  for (i = 0; i < n; i++)
    scanf("%d", &arr[i]);
 
  printf("\nARRAY  : ");
  print(&arr[0], n);
 
  radixsort(&arr[0], n);
 
  printf("\nSORTED : ");
  print(&arr[0], n);
  printf("\n");
 
  return 0;
}
