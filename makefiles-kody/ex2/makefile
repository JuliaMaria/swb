# Main makefile

main: main.o dbgPrint.o
	g++ obj/main.o obj/dbgPrint.o -o bin/$@

main.o: main.cpp main.h
	g++ -c -Wall $< -o obj/$@

dbgPrint.o: dbgPrint.cpp dbgPrint.h
	g++ -c -Wall $< -o obj/$@

.PHONY: clean
clean:
	rm -f *.o main
	rm -f obj/*
	rm -f bin/*
