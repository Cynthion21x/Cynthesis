#pragma once
#include <SDL2/SDL.h>
#include "camera.h"
#include "utils/entityList.h"

class Core {

    public:

        Core();
        ~Core();

        inline bool running() {return _running;};

        void Events();
        void Update();
        void Render();

    private:

        EntityList* entities;
        Camera* camera;
        bool _running;

        SDL_Window* window;

};