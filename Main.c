#include <stdio.h>

int main(void)
{
  int a, n;
  printf("plz enter the number of lines:");
  scanf("%d", &n);
  printf("1\n");
  for (a = 1; a < n; a++){
    int counter = 0;
    while (counter <= a){
      int track1 = 1, mua = a;
      for (; mua != 0; mua-- ){
        track1 = track1 * mua;
      }
      int track2 = 1, mua2 = counter;
      for (; mua2 != 0; track2 = track2 * mua2--);
      int track3 = 1, mua3 = a - counter;
      for (; mua3 != 0; track3 = track3 * mua3--);
      printf("%d ", track1/(track2*track3));
      counter += 1;
    }
    printf("\n");
  }
  return 0;
}
