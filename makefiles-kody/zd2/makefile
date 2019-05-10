# Main makefile
CC:=g++
CFLAGS:=-c -Wall

all: install

install: main

sortowanie.o: src/sortowanie.cpp src/sortowanie.h
	$(CC) $(CFLAGS) $< -o $@

cw7_dom1.o: src/cw7_dom1.cpp
	$(CC) $(CFLAGS) $< -o $@

main: libs/libswbmath/swbmath.o sortowanie.o cw7_dom1.o
	$(CC) $(CFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f main
	rm -f obj/*
