"""FizzBuzz – Tests (werden VOR der Implementierung geschrieben)."""

import unittest

from fizzbuzz import fizzbuzz, fizzbuzz_range


class FizzBuzzTest(unittest.TestCase):
    """Tests für die FizzBuzz-Kata.

    Regel:
      - Teilbar durch 3   -> "Fizz"
      - Teilbar durch 5   -> "Buzz"
      - Teilbar durch 7   -> "Zuzz"
      - Teilbar durch 3 und 5 -> "FizzBuzz"
      - Teilbar durch 3 und 7 -> "FizzZuzz"
      - Teilbar durch 5 und 7 -> "BuzzZuzz"
      - Teilbar durch 3, 5 und 7 -> "FizzBuzzZuzz"
      - Sonst             -> die Zahl als String
    """

    def test_zahl_ohne_teiler_bleibt_zahl(self):
        self.assertEqual(fizzbuzz(1), "1")

    def test_vier_bleibt_vier(self):
        self.assertEqual(fizzbuzz(4), "4")

    def test_teiler_3_gibt_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(27), "Fizz")

    def test_teiler_5_gibt_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(50), "Buzz")

    def test_teiler_3_und_5_gibt_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")

    def test_einhundert_gibt_fizzbuzz(self):
        self.assertEqual(fizzbuzz(100), "Buzz")

    def test_sechzig_gibt_fizzbuzz(self):
        self.assertEqual(fizzbuzz(60), "FizzBuzz")

    def test_teiler_7_gibt_zuzz(self):
        self.assertEqual(fizzbuzz(7), "Zuzz")
        self.assertEqual(fizzbuzz(14), "Zuzz")
        self.assertEqual(fizzbuzz(98), "Zuzz")

    def test_teiler_3_und_7_gibt_fizzzuzz(self):
        self.assertEqual(fizzbuzz(21), "FizzZuzz")
        self.assertEqual(fizzbuzz(63), "FizzZuzz")

    def test_teiler_5_und_7_gibt_buzzzuzz(self):
        self.assertEqual(fizzbuzz(35), "BuzzZuzz")
        self.assertEqual(fizzbuzz(70), "BuzzZuzz")

    def test_teiler_3_5_und_7_gibt_fizzbuzzzuzz(self):
        self.assertEqual(fizzbuzz(105), "FizzBuzzZuzz")
        self.assertEqual(fizzbuzz(210), "FizzBuzzZuzz")


class FizzBuzzRangeTest(unittest.TestCase):
    """Tests für die Bereichs-Variante fizzbuzz_range."""

    def test_standardbereich_ist_1_bis_100(self):
        ergebnis = fizzbuzz_range()
        self.assertEqual(len(ergebnis), 100)
        self.assertEqual(ergebnis[0], "1")
        self.assertEqual(ergebnis[-1], "Buzz")

    def test_kleine_bereich_ist_richtig(self):
        self.assertEqual(
            fizzbuzz_range(1, 5),
            ["1", "2", "Fizz", "4", "Buzz"],
        )

    def test_bereich_enthaelt_fizzbuzz_an_position_15(self):
        ergebnis = fizzbuzz_range(1, 20)
        self.assertEqual(ergebnis[14], "FizzBuzz")
        self.assertEqual(ergebnis[19], "Buzz")

    def test_bereich_enthaelt_zuzz_an_positionen_7_21_35(self):
        ergebnis = fizzbuzz_range(1, 35)
        self.assertEqual(ergebnis[6], "Zuzz")
        self.assertEqual(ergebnis[20], "FizzZuzz")
        self.assertEqual(ergebnis[34], "BuzzZuzz")


if __name__ == "__main__":
    unittest.main()
