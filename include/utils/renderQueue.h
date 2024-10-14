#pragma once
#include <iostream>
#include "entities/entity.h"

class RenderQueue {

    public:

        RenderQueue();
        ~RenderQueue();

        void add(Entity data);
        Entity remove();

        inline bool isEmpty() { return front == nullptr; };

    private:

        int size;
        node* front;
        node* back;

};

class node {

    public:

        node(Entity data);
        node* next;

        inline Entity value() { return _data; }

    private:

        Entity _data;

};