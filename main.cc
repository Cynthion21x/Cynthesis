#include <iostream>
#define SDL_MAIN_HANDLED
#include "core.h"

int main(int argsc, char* argsv[]) {

    Core* simulation = new Core();

    while(simulation->running()) {

        simulation->Events();
        simulation->Update();
        simulation->Render();

    }

    delete simulation;

    return 0;

}