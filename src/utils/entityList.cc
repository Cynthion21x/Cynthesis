#include "utils/entityList.h"

EntityList::EntityList() {

    head = nullptr;

}

EntityList::~EntityList() {
    clear();
}

void EntityList::clear() {
    while (head != nullptr) {
        node* temp = head;
        head = head->next;
        delete temp;
    }
}

int EntityList::entityCount() {
    int count = 0;
    node* current = head;
    while (current != nullptr) {
        count++;
        current = current->next;
    }
    return count;
}

bool EntityList::addEntity(Entity data) {
    node* newNode = new node(data);
    if (head == nullptr) {
        head = newNode;
    } else {
        node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    return true;
}

bool EntityList::removeEntity(int index) {
    if (index < 0 || head == nullptr) {
        return false;
    }

    node* temp = head;

    if (index == 0) {
        head = head->next;
        delete temp;
        return true;
    }

    node* prev = nullptr;
    for (int i = 0; temp != nullptr && i < index; ++i) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == nullptr) {
        return false;
    }

    prev->next = temp->next;
    delete temp;
    return true;
}