# Main makefile
CC:=g++
CFLAGS:=-c -Wall

all: install

install: swbmath.o

%.o: %.cpp %.h 
	$(CC) $(CFLAGS) $< -o $@

swbmath.o: %.o
	$(CC) $(CFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f %.o
