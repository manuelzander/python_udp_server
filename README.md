# zoe_challenge

## Prerequisites

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

The code is run and tested with Python 3.7.7 on macOS 10.14.6.

### Environment

Clone the repo to your local machine.

Create a virtual environment for Python 3 with:

    python3 -m pip install virtualenv
    python3 -m virtualenv -p python3 env

Activate the virtual environment with:

    source env/bin/activate

Install the required Python packages with:

    pip3 install -r requirements.txt

## Run the app without Docker

Quickstart (see below for flags, or use `-h`):

    python3 app.py

## Run the app with Docker

Make sure you have Docker installed locally:

    docker -v
    
Quickstart:

    make build && make run

Alternatively, build the image locally with:

    docker build --tag emoji-app:latest .
    
Or:

    make build

Then, run the container locally with:
    
    docker run --rm --name emoji-app -p 3001:3001/udp emoji-app:latest

Or:

    make run

Optionally, the following flags can be used: `--n`, `--r`, `--s` and `--h/-h`:

* `--n` Multiply number of emojis by n (`int`, default: `1`)
* `--r` Disable translation from keyword to emoji (`bool`, default: `False`)
* `--s` Separator between each emoji (`str`, default: `""`)
* `--h/-h` See usage information

For example:

    docker run --rm --name emoji-app -p 3001:3001/udp emoji-app:latest --n 2 --r True --s "+"
    
In another shell session, you can now trigger the endpoint (`0.0.0.0:3001`), for example using `nc`:

    nc -u 0.0.0.0 3001

Send a message and hit enter:

    2 :ok:

## Development and testing

Using the `Makefile` you can run `make <cmd>` where `<cmd>` is one of:

* `sort-imports` to ensure Python imports are in the correct PEP format
* `format` to format Python files using black
* `type-check` to run `mypy` static type checking
* `test` to run unittests using `pytest`
* `all` to run all the above steps

or just type `make`/`make all`, which will run all of the above.

## Authors

* Manuel Zander
