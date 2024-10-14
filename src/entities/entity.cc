#include "entities/entity.h"

Entity::Entity() {

    id = -1;
    x = 0;
    y = 0;
    w = 0;
    h = 0;

}

Entity::Entity(int _id, int _x, int _y, int _w, int _h) {

    id = _id;
    x = _x;
    y = _y;
    w = _w;
    h = _h;

}

Entity::~Entity() {


}