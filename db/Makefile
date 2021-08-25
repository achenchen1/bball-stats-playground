CFLAGS?=-lsqlite3 -std=c99
CC=gcc

default: all

all: test
	
test: test.c
	$(CC) $(CFLAGS) -o test.o $<

clean:
	rm test.o
