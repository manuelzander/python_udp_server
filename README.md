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


## Run the app

The `Dockerfile` can be used to build an image and deploy it locally:
Make sure you have Docker installed:

    docker -v
    
Build the image with:

    docker build --tag emoji-app:latest .
    
Run the container locally:
    
    docker run --name emoji-app:latest -p 3001:3001 app
    
You can now trigger the endpoint (`localhost:3001`), for example using `nc`.

<!-- TODO -->
<!-- Include usage info -->

## Development and testing

Use the `Makefile` you can run `make <cmd>` where `<cmd>` is one of:

* `sort-imports` to ensure Python imports are in the correct PEP format
* `format` to format Python files using black
* `type-check` to run `mypy` static type checking
* `test` to run unittests using `pytest`
* `all` to run all the above steps

or just type `make`/`make all`, which will run all of the above.

## Authors

* Manuel Zander