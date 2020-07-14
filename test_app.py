#!/usr/bin/env python

import unittest

import app


class AppTestCase(unittest.TestCase):
    def test_base_case_thumbsup(self) -> None:
        app.multiplier = 1
        app.separator = ""
        app.translation_toggle = False
        self.assertEqual(app.generate_response("1 :thumbsup:"), "👍")

    def test_base_case_thumbsdown(self) -> None:
        app.multiplier = 1
        app.separator = ""
        app.translation_toggle = False
        self.assertEqual(app.generate_response("2 :thumbsdown:"), "👎👎")

    def test_base_case_ok(self) -> None:
        app.multiplier = 1
        app.separator = ""
        app.translation_toggle = False
        self.assertEqual(app.generate_response("5 :ok:"), "👌👌👌👌👌")

    def test_base_case_crossed(self) -> None:
        app.multiplier = 1
        app.separator = ""
        app.translation_toggle = False
        self.assertEqual(app.generate_response("10 :crossed:"), "🤞🤞🤞🤞🤞🤞🤞🤞🤞🤞")

    def test_separator_1_thumbsup(self) -> None:
        app.multiplier = 1
        app.separator = ","
        app.translation_toggle = False
        self.assertEqual(app.generate_response("1 :thumbsup:"), "👍")

    def test_separator_2_thumbsup(self) -> None:
        app.multiplier = 1
        app.separator = ","
        app.translation_toggle = False
        self.assertEqual(app.generate_response("2 :thumbsup:"), "👍,👍")

    def test_separator_3_thumbsup(self) -> None:
        app.multiplier = 1
        app.separator = ","
        app.translation_toggle = False
        self.assertEqual(app.generate_response("3 :thumbsup:"), "👍,👍,👍")

    def test_no_translation_1_thumbsup(self) -> None:
        app.multiplier = 1
        app.separator = ""
        app.translation_toggle = True
        self.assertEqual(app.generate_response("1 :thumbsup:"), ":thumbsup:")

    def test_no_translation_2_thumbsup(self) -> None:
        app.multiplier = 1
        app.separator = ""
        app.translation_toggle = True
        self.assertEqual(app.generate_response("2 :thumbsup:"), ":thumbsup::thumbsup:")

    def test_no_translation_3_thumbsup(self) -> None:
        app.multiplier = 1
        app.separator = ""
        app.translation_toggle = True
        self.assertEqual(
            app.generate_response("3 :thumbsup:"), ":thumbsup::thumbsup::thumbsup:"
        )

    def test_multiplier_2_thumbsup(self) -> None:
        app.multiplier = 2
        app.separator = ""
        app.translation_toggle = False
        self.assertEqual(app.generate_response("1 :thumbsup:"), "👍👍")

    def test_multiplier_3_thumbsup(self) -> None:
        app.multiplier = 3
        app.separator = ""
        app.translation_toggle = False
        self.assertEqual(app.generate_response("1 :thumbsup:"), "👍👍👍")

    def test_multiplier_5_thumbsup(self) -> None:
        app.multiplier = 5
        app.separator = ""
        app.translation_toggle = False
        self.assertEqual(app.generate_response("1 :thumbsup:"), "👍👍👍👍👍")

    def test_complex_ok_1(self) -> None:
        app.multiplier = 2
        app.separator = "++"
        app.translation_toggle = False
        self.assertEqual(app.generate_response("2 :ok:"), "👌++👌++👌++👌")

    def test_complex_ok_2(self) -> None:
        app.multiplier = 3
        app.separator = " "
        app.translation_toggle = True
        self.assertEqual(
            app.generate_response("2 :ok:"), ":ok: :ok: :ok: :ok: :ok: :ok:"
        )

    def test_complex_ok_2(self) -> None:
        app.multiplier = 3
        app.separator = " "
        app.translation_toggle = True
        self.assertEqual(
            app.generate_response("2 :ok:"), ":ok: :ok: :ok: :ok: :ok: :ok:"
        )

    def test_failure(self) -> None:
        val = "x"
        self.assertEqual(app.generate_response(val), f"Unknown command: {val}")

    def test_failure(self) -> None:
        val = "x :ok:"
        self.assertEqual(app.generate_response(val), f"Unknown command: {val}")

    def test_failure(self) -> None:
        val = "1 :okokokokok:"
        self.assertEqual(app.generate_response(val), f"Unknown command: {val}")


if __name__ == "__main__":
    unittest.main()
