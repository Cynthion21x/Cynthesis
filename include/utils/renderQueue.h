#pragma once
#include <iostream>
#include "entities/entity.h"
#include "utils/node.h"

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