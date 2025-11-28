#pragma once

typedef struct Coordinate {
  int x;
  int y;
  int z;
} coordinate_t;

coordinate_t coord(int x, int y, int z);

coordinate_t reduce_cords(coordinate_t coord, int r);
