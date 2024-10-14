#pragma once

class Entity {

    public:

        Entity();
        Entity(int id, int _x, int _y, int _w, int _h);
        ~Entity();

        int id;

        float x, y;
        float w, h;

};