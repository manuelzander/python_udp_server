#!/usr/bin/env python

import asyncio
import logging

import coloredlogs

from utils import create_parser

logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")

# App settings
APP_HOST = "0.0.0.0"
APP_PORT = 3001

TRANSLATION_TABLE = {
    ":thumbsup:": "👍",
    ":thumbsdown:": "👎",
    ":ok:": "👌",
    ":crossed:": "🤞",
}

# For further reference see https://docs.python.org/3.7/library/asyncio-protocol.html#udp-echo-client
class MessagePrinterServerProtocol(asyncio.BaseProtocol):
    def __init__(self, n: int, s: str, r: bool) -> None:
        super().__init__()
        self.multiplier = n
        self.separator = s
        self.translation_toggle = r

    def connection_made(self, transport) -> None:  # type: ignore
        self.transport = transport

    def datagram_received(self, data, addr) -> None:  # type: ignore
        message = data.decode()
        logger.debug(f"Received message: '{message}' from addr: {addr}")

        formatted_message = format_message(
            message, self.multiplier, self.separator, self.translation_toggle
        )

        # Print main output of application to stdout
        print(formatted_message)


def handle_error(message: str) -> str:
    logger.warning(f"Unknown command: {message}")
    return f"Unknown command: {message}"


def format_message(
    message: str, multiplier: int, separator: str, translation_toggle: bool
) -> str:
    logger.debug(f"Formatting message: {message}")

    params = message.split()

    if len(params) > 2:
        return handle_error(message)

    try:
        nb_repetitions, command = int(params[0]), params[1]
        text = TRANSLATION_TABLE[command]
    except (ValueError, KeyError, IndexError):
        return handle_error(message)

    response = (
        nb_repetitions * multiplier * [text if not translation_toggle else command]
    )

    formatted_message = separator.join(response)
    logger.debug(f"Formatted message: '{formatted_message}'")
    return formatted_message


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    logger.debug(f"Running with args: n: {args.n}, s: {args.s}, r: {args.r}")
    logger.info(f"Starting UDP server listening on: {APP_HOST}:{APP_PORT}")

    loop = asyncio.get_event_loop()
    transport, protocol = loop.run_until_complete(
        loop.create_datagram_endpoint(
            lambda: MessagePrinterServerProtocol(args.n, args.s, args.r),
            local_addr=(APP_HOST, APP_PORT),
        )
    )

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        transport.close()
        loop.close()


if __name__ == "__main__":
    logger.debug(f"Running {__file__}")
    logger.debug(f"APP_PORT: {APP_PORT}")
    main()
