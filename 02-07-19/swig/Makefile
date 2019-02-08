#
# Build SWIG files.
#
# Copyright (c) 2019, Sekhar Ravinutala.
#

INC=-I/usr/include/python3.7m

hello/_greeting.so: hello/greeting.cpp hello/greeting_wrap.cxx
	g++ -o $@ -fPIC -shared ${INC} $^

hello/greeting_wrap.cxx: hello/greeting.i hello/greeting.h
	swig -c++ -python $<

clean:
	rm -f hello/_greeting.so hello/greeting_wrap.cxx hello/greeting.py