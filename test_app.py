#!/usr/bin/env python

import unittest

import app


class AppTestCase(unittest.TestCase):
    def test_handle_error(self) -> None:
        self.assertEqual(app.handle_error("message"), "Unknown command: message")

    def test_base_case_thumbsup(self) -> None:
        self.assertEqual(app.format_message("1 :thumbsup:", 1, "", False), "👍")

    def test_base_case_thumbsdown(self) -> None:
        self.assertEqual(app.format_message("2 :thumbsdown:", 1, "", False), "👎👎")

    def test_base_case_ok(self) -> None:
        self.assertEqual(app.format_message("5 :ok:", 1, "", False), "👌👌👌👌👌")

    def test_base_case_crossed(self) -> None:
        self.assertEqual(app.format_message("10 :crossed:", 1, "", False), "🤞🤞🤞🤞🤞🤞🤞🤞🤞🤞")

    def test_separator_1_thumbsup(self) -> None:
        self.assertEqual(app.format_message("1 :thumbsup:", 1, ",", False), "👍")

    def test_separator_2_thumbsup(self) -> None:
        self.assertEqual(app.format_message("2 :thumbsup:", 1, ",", False), "👍,👍")

    def test_separator_3_thumbsup(self) -> None:
        self.assertEqual(app.format_message("3 :thumbsup:", 1, ",", False), "👍,👍,👍")

    def test_no_translation_1_thumbsup(self) -> None:
        self.assertEqual(app.format_message("1 :thumbsup:", 1, "", True), ":thumbsup:")

    def test_no_translation_2_thumbsup(self) -> None:
        self.assertEqual(
            app.format_message("2 :thumbsup:", 1, "", True), ":thumbsup::thumbsup:"
        )

    def test_no_translation_3_thumbsup(self) -> None:
        self.assertEqual(
            app.format_message("3 :thumbsup:", 1, "", True),
            ":thumbsup::thumbsup::thumbsup:",
        )

    def test_multiplier_2_thumbsup(self) -> None:
        self.assertEqual(app.format_message("1 :thumbsup:", 2, "", False), "👍👍")

    def test_multiplier_3_thumbsup(self) -> None:
        self.assertEqual(app.format_message("1 :thumbsup:", 3, "", False), "👍👍👍")

    def test_multiplier_5_thumbsup(self) -> None:
        self.assertEqual(app.format_message("1 :thumbsup:", 5, "", False), "👍👍👍👍👍")

    def test_complex_ok_1(self) -> None:
        self.assertEqual(app.format_message("2 :ok:", 2, "++", False), "👌++👌++👌++👌")

    def test_complex_ok_2(self) -> None:
        self.assertEqual(
            app.format_message("2 :ok:", 3, " ", True), ":ok: :ok: :ok: :ok: :ok: :ok:"
        )

    def test_complex_ok_2(self) -> None:
        self.assertEqual(
            app.format_message("2 :ok:", 3, " ", True), ":ok: :ok: :ok: :ok: :ok: :ok:"
        )

    def test_failure(self) -> None:
        val = ""
        self.assertEqual(
            app.format_message(val, 1, "", False), f"Unknown command: {val}"
        )

    def test_failure_1(self) -> None:
        val = "x"
        self.assertEqual(
            app.format_message(val, 1, "", False), f"Unknown command: {val}"
        )

    def test_failure_2(self) -> None:
        val = "x :ok:"
        self.assertEqual(
            app.format_message(val, 1, "", False), f"Unknown command: {val}"
        )

    def test_failure_3(self) -> None:
        val = "1 :okokokokok:"
        self.assertEqual(
            app.format_message(val, 1, "", False), f"Unknown command: {val}"
        )

    def test_failure_4(self) -> None:
        val = "1 :ok: :ok:"
        self.assertEqual(
            app.format_message(val, 1, "", False), f"Unknown command: {val}"
        )


if __name__ == "__main__":
    unittest.main()
