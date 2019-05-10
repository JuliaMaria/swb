#TODO - Add variables here - compiler, flags...
CC=g++
CFLAGS=-c -Wall

BINDIR=bin
SRCDIR=src
OBJDIR=obj
DSTDIR=..

all: build install

build: $(OBJDIR)/libPrint.o
	ar rvs libPrint.a $<
	#TODO - FILL ME! Create library

$(OBJDIR)/libPrint.o: $(SRCDIR)/libPrint.cpp libPrint.h
	$(CC) $(CFLAGS) $< -o $@
	#TODO - FILL ME! Build .o file.

install: $(DSTDIR)/libPrint.a 

$(DSTDIR)/libPrint.a: $(OBJDIR)/libPrint.o
	cp $< $@
	#TODO - FILL ME! Copy lib from bin dir to destination directory - ../


.PHONY: clean
clean:
	rm -f *.a *.o
	rm -f obj/*
	rm -f bin/*
	#TODO - FILL ME! Add removal of .o files and ./bin/*

