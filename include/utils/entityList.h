#pragma once
#include "entities/entity.h"
#include "utils/node.h"

class EntityList {

    public:

        EntityList();
        ~EntityList();

        int entityCount();
        void clear();

        bool addEntity(Entity data);
        Entity* getEntity(int index);
        bool removeEntity(int index);

    private:

        node* head;

};