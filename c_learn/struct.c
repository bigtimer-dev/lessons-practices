#include "struct.h"

coordinate_t coord(int x, int y, int z) {
  coordinate_t c = {.x = x, .y = y, .z = z};
  return c;
}

coordinate_t reduce_cords(coordinate_t coord, int r) {
  coordinate_t new_cords = coord;
  new_cords.x -= r;
  new_cords.y -= r;
  new_cords.z -= r;
  return new_cords;
}
