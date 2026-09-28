#!/bin/bash

if [ -f "./.venv/bin/activate" ]; then
    echo Setup has already been run. Enter venv with "source .venv/bin/activate" or destroy it first with "make erase-venv"
    exit
fi

make init
if [ -f "./.venv/bin/activate" ]; then
    echo "Entering virtual environment..."
    exec bash --rcfile <(echo "source ~/.bashrc; \
    source ./.venv/bin/activate; \
    echo Installing project tools and dependencies...; \
    make get-tools; \
    make get-dependencies; \
    echo Exit the virtual environment by running \"deactivate\" \
    ")
fi