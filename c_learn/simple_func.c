#include "struct.h"
#include <stdio.h>

int main() {
  printf("this is a simple output print\n");
  coordinate_t cord = coord(3, 5, 6);
  printf("first cord\n");
  printf("x: %d, y: %d, z: %d\n", cord.x, cord.y, cord.z);
  printf("second cord\n");
  cord = coord(5, 3, 10);
  printf("x: %d, y: %d, z: %d\n", cord.x, cord.y, cord.z);
  printf("third cord\n");
  cord = coord(10, 11, 23);
  printf("x: %d, y: %d, z: %d\n", cord.x, cord.y, cord.z);
  int reduce = 4;
  cord = reduce_cords(cord, reduce);
  printf("reduce by %d\n", reduce);
  printf("x: %d, y: %d, z: %d\n", cord.x, cord.y, cord.z);
  coordinate_t *ptr = &cord;
  ptr->x = 10;
  printf("printing a pointer values: x:%d y:%d z:%d\n", ptr[0].x, ptr[0].y,
         ptr[0].z);
  ptr->y = 23;
  printf("other way to print pointer x:%d y:%d z:%d \n", (ptr + 0)->x,
         (ptr + 0)->y, (ptr + 0)->z);
  coordinate_t my_array[3] = {coord(1, 2, 4), coord(3, 4, 6), coord(5, 3, 6)};
  for (int i = 0; i < 3; i += 1) {
    printf("this is %d coord\n", i + 1);
    printf("x: %d y: %d z: %d \n", my_array[i].x, my_array[i].y, my_array[i].z);
    printf("other way of printing the values in each memory adress\n");
    int *ptr2 = (int *)
        my_array; // pointer change to reference the adress pointer of my_array
    for (int i = 0; i < 9; i += 1) {
      printf("my_array[%d]= %d\n", i, ptr2[i]);
    }
  }
  return 0;
}
