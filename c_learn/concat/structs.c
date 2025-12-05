#include "structs.h"
#include <stdio.h>
#include <string.h>

int smart_append(textbuffer_t *dest, const char *src) {
  if (!dest || !src)
    return 1;
  const int max_buffer = 100;
  size_t len_src = strlen(src);
  int avaliable_memory = max_buffer - dest->length - 1;
  if (avaliable_memory < len_src) {
    strncat(dest->buffer, src, avaliable_memory);
    dest->length = max_buffer - 1;
    return 1;
  } else {
    strcat(dest->buffer, src);
    dest->length += len_src;
    return 0;
  }
}
