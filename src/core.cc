#include "core.h"

Core::Core() {

    _running = true;

    if(SDL_Init(SDL_INIT_VIDEO) < 0 ) {
        std::cout << "SDL could not initialize! SDL_Error: %s\n" << SDL_GetError() << std::endl;
    }

    window = SDL_CreateWindow("Cynthesis", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 640, 480, SDL_WINDOW_SHOWN);
    camera = new Camera(640, 480, window);

    entities = new EntityList();

}

Core::~Core() {

    delete entities;
    delete camera;

    SDL_DestroyWindow(window);
    SDL_Quit();
    
}

void Core::Events() {

    SDL_Event event;

    while (SDL_PollEvent(&event)) {
        if (event.type == SDL_QUIT) {
            _running = false;
        }
    }

}

void Core::Render() {

    camera->draw();

}

void Core::Update() {

}