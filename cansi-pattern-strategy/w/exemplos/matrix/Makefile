#
# Makefile
APP = ../../u/app.py
YML = array.yml

SRCS    = $(wildcard *.c)
OBJECTS = $(foreach s,$(SRCS), $(s:.c=.o))
HEADERS = $(wildcard *.h)

main: $(OBJECTS)
	$(CC) -o $@ $^
run: main
	./main
clean:
	/bin/rm $(OBJECTS)

$(OBJECTS): ${HEADERS}

tags: $(SRCS) $(HEADERS)
	$(CC) -M $<                        | \
	sed -e 's/[\\ ]/\n/g'              | \
	sed -e '/^$/d' -e '/\.o:[ \t]*$/d' | \
	ctags -L - --c++-kinds=+p --fields=+iaS --extra=+q
gen:
	python $(APP) -s -y $(YML)
valgrind:
	valgrind ./main
