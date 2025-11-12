#
# Makefile
#
#
APP = ../../app.py
YML = test.yml

SRCS    = $(wildcard *.c)
OBJECTS = $(foreach s,$(SRCS), $(s:.c=.o))
HEADERS = $(wildcard *.h)

main: $(OBJECTS)
	$(CC) -o $@ $^
run: main
	./main

reset:
	@(ls | grep -vE '(main.c|Makefile|*.yml)'| xargs rm)
	@make gen
clean:
	/bin/rm $(OBJECTS)

$(OBJECTS): ${HEADERS}

valgrind:
	valgrind ./main
gen:
	python $(APP) -s -y $(YML)|sort

