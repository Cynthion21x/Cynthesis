#include "utils/renderQueue.h"

RenderQueue::RenderQueue() {

    size = 0;
    front = nullptr;
    back = nullptr;

}

RenderQueue::~RenderQueue() {

    while(!isEmpty()) {

        remove();

    }

}

Entity RenderQueue::remove() {

    if (isEmpty()) {
        std::cout << "Render Queue Empty!" << std::endl;
        return Entity();
    }

    Entity value = front->value();
    node* temp = front;
    front = front->next;

    delete temp;

    size--;

    if (front == nullptr) {
        back = nullptr;
    }

    return value;

}

void RenderQueue::add(Entity data) {

    node* newNode = new node(data);

    if (isEmpty()) {

        front = back = newNode;

    } else {

        back->next = newNode;
        back = newNode;

    }

    size++;

}