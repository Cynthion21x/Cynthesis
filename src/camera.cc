#include "camera.h"

Camera::Camera() { }

Camera::Camera(int _w, int _h, SDL_Window* window) {

    x = 0;
    y = 0;

    w = _w;
    h = _h;

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    SDL_RenderPresent(renderer);

    renderingQueue = new RenderQueue();

}

Camera::~Camera() {

    SDL_DestroyRenderer(renderer);
    delete renderingQueue;

}

void Camera::draw() {

    while (!renderingQueue->isEmpty()) {

        Entity target = renderingQueue->remove();

        SDL_Rect dstRect;
        dstRect.x = target.x - x;
        dstRect.y = target.y - y;
        dstRect.w = target.w;
        dstRect.h = target.h;

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderDrawRect(renderer, &dstRect);

        //Draw Entity

    }

}