#pragma once
#include <string.h>

typedef struct {
  size_t length;
  char buffer[100];
} textbuffer_t;

int smart_append(textbuffer_t *dest, const char *src);
