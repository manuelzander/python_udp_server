#!/usr/bin/env python

import asyncio
import logging
from typing import Any, Union

import coloredlogs

from utils import create_parser

logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


# App settings
APP_PORT = 3001
TIME_SERVE_SECONDS = 3600  # Serve for 1 hour

TRANSLATION_TABLE = {
    ":thumbsup:": "👍",
    ":thumbsdown:": "👎",
    ":ok:": "👌",
    ":crossed:": "🤞",
}

# Need these for static type checking with mypy
multiplier: int
separator: str
translation_toggle: bool


# For further reference see https://docs.python.org/3.7/library/asyncio-protocol.html#udp-echo-client
class EchoServerProtocol(asyncio.BaseProtocol):
    def __init__(self) -> None:
        super().__init__()

    def connection_made(self, transport) -> None:  # type: ignore
        self.transport = transport

    def datagram_received(self, data, addr) -> None:  # type: ignore
        message = data.decode()
        logger.debug(f"Received message: '{message}' from addr: {addr}")
        response = generate_response(message)
        logger.debug(f"Generated response: '{response}'")
        print(response)


def generate_response(message: str) -> Union[str, Any]:
    logger.debug(f"Generating response for message: {message}")

    try:
        params = message.split()
        int(params[0])
    except Exception as e:
        logger.error(f"Unknown command: {message}")
        return f"Unknown command: {message}"

    if params[1] not in TRANSLATION_TABLE:
        logger.error(f"Unknown command: {message}")
        return f"Unknown command: {message}"

    number = int(params[0]) * multiplier
    text = TRANSLATION_TABLE[params[1]] if not translation_toggle else params[1]
    repsonse = number * [text]
    return separator.join(repsonse)


async def start_udp_server(host: str = "0.0.0.0", port: int = APP_PORT) -> None:
    logger.info(f"Starting UDP server listening on: {host}:{port}")

    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(), local_addr=(host, port)
    )

    try:
        await asyncio.sleep(TIME_SERVE_SECONDS)
    finally:
        transport.close()


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    logger.debug(f"Running with args: n: {args.n}, s: {args.s}, r: {args.r}")

    global multiplier, separator, translation_toggle
    multiplier = args.n
    separator = args.s
    translation_toggle = args.r

    asyncio.run(start_udp_server())


if __name__ == "__main__":
    logger.debug(f"Running {__file__}")
    logger.debug(f"APP_PORT: {APP_PORT}")
    main()
