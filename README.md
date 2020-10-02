# Python UDP server using asyncio

![status](https://img.shields.io/github/workflow/status/manuelzander/python_udp_server/python_udp_server/master?label=actions&logo=github&style=for-the-badge) ![last-commit](https://img.shields.io/github/last-commit/manuelzander/python_udp_server/master?logo=github&style=for-the-badge) ![issues-pr-raw](https://img.shields.io/github/issues-pr-raw/manuelzander/python_udp_server?label=open%20prs&logo=github&style=for-the-badge) ![release](https://img.shields.io/github/v/release/manuelzander/python_udp_server?&style=for-the-badge) [![license](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

This small project comprises a simple Python UDP server plus Dockerfile, as well as a (hopefully) useful Makefile and unittests.

The server makes use of the `asyncio` library to allow for asynchronous request handling.

## Prerequisites

![python](https://img.shields.io/badge/python-3.7-blue?style=for-the-badge&logo=python&logoColor=white) ![python-2](https://img.shields.io/badge/python-3.8-blue?style=for-the-badge&logo=python&logoColor=white)

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

The code is run and tested with Python 3.7.7 on macOS 10.14.6 and Python 3.8.5 on Ubuntu 18.04.5.

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

Stop with Ctrl+C.

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

* `sort-imports` to ensure Python imports are in the correct PEP format/order
* `format` to format Python files using `black`
* `type-check` to run static type checking using `mypy`
* `test` to run unittests using `pytest`
* `all` to run all steps (or just type `make`)

## Authors

* Manuel Zander

## Acknowledgments

Many thanks to [julvo](https://github.com/julvo) for his review and great suggestions during development of this software 😊
