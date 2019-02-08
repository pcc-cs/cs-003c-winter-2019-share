/**
* Common SWIG interface file for all target languages.
*/

%include <std_string.i>

%module greeting
%{
#include "greeting.h"
%}

%include "greeting.h"