#pragma once
#include <SDL2/SDL.h>
#include "utils/renderQueue.h"

class Camera {

    public:

        Camera();
        Camera(int w, int h, SDL_Window* window);
        ~Camera();

        RenderQueue* renderingQueue;

        void draw();

        int x, y;
        int w, h;

    private:

        SDL_Renderer* renderer;

};