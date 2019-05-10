# Main makefile
CC:=g++
CFLAGS:=-c -Wall
OBJDIR:=obj
SRCDIR:=src

all: install

install: $(OBJDIR)/main

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp $(SRCDIR)/%.h | $(OBJDIR) 
	$(CC) $(CFLAGS) $< -o $@

$(OBJDIR)/main: $(OBJDIR)/%.o
	$(CC) $(CFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f main
	rm -f obj/*
