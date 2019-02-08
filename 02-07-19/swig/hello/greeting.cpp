/**
 * Hello implementation.
 * 
 * Copyright (c) 2019, Sekhar Ravinutala.
 */

#include "greeting.h"

std::string greeting(std::string name) {
    /**
     * Return a message built on name.
     * - name: Name, optional.
     */
    return name.compare("") == 0 ? "Surely, you have a name?" : "Hello, " + name;
}