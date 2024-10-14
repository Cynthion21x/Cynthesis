#pragma once
#include <SDL2/SDL.h>
#include "camera.h"

class Core {

    public:

        Core() {}
        ~Core() {}

        inline bool running() {return _running;};

        void Events();
        void Update();
        void Render();

    private:

        SDL_Window* window;
        SDL_Surface* surface;
        bool _running;

};