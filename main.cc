#include <iostream>
#include <SDL2/SDL.h>
#include "core.h"

int main(int argsc, char* argsv[]) {

    if(SDL_Init(SDL_INIT_VIDEO) < 0 ) {
        std::cout << "SDL could not initialize! SDL_Error: %s\n" << SDL_GetError() << std::endl;
    }

    return 0;

}