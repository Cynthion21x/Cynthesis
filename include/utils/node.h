#pragma once
#include "entities/entity.h"

class node {

    public:

        node(Entity data);
        node* next;

        inline Entity value() { return _data; }

    private:

        Entity _data;

};