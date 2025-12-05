#include "structs.h"
#include <stdio.h>
#include <string.h>

int main() {
  const char *my_string = "hello my friend. how are you today?";
  textbuffer_t my_buffer = {0};
  smart_append(&my_buffer, my_string);
  printf("buffer string: %s\n", my_buffer.buffer);
  const char *my_string2 = " fine and you?";
  smart_append(&my_buffer, my_string2);
  printf("buffer string after concat something else: %s\n and the length of "
         "the string is: %zu\n",
         my_buffer.buffer, my_buffer.length);
  return 0;
}
