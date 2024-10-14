#pragma once
#include <SDL2/SDL.h>
#include "utils/renderQueue.h"

class Camera {

    public:

        Camera();
        ~Camera();

        RenderQueue renderingQueue;

        void draw(SDL_Surface* surface);

};