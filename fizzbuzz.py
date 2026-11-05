"""FizzBuzz – Implementierung."""

# Jede Regel steht genau einmal hier: (Teiler, Wort), in Ausgabe-Reihenfolge.
REGELN: list[tuple[int, str]] = [
    (3, "Fizz"),
    (5, "Buzz"),
    (7, "Zuzz"),
]


def teilwort(n: int, teiler: int, wort: str) -> str:
    """Rückt ``wort`` zurück, falls ``n`` durch ``teiler`` teilbar ist, sonst "".

    >>> teilwort(21, 3, "Fizz")
    'Fizz'
    >>> teilwort(22, 3, "Fizz")
    ''
    """
    return wort if n % teiler == 0 else ""


def fizzbuzz(n: int) -> str:
    """Rückt für die Zahl ``n`` das FizzBuzz-Ergebnis zurück.

    Jede Regel aus :data:`REGELN` wird genau einmal geprüft; alle
    passenden Wörter werden in der Reihenfolge von ``REGELN``
    zusammengeklebt:

      - Teilbar durch 3   -> "Fizz"
      - Teilbar durch 5   -> "Buzz"
      - Teilbar durch 7   -> "Zuzz"
      - 21  (3·7)         -> "FizzZuzz"
      - 35  (5·7)         -> "BuzzZuzz"
      - 105 (3·5·7)       -> "FizzBuzzZuzz"
      - Sonst             -> die Zahl als String

    >>> fizzbuzz(7)
    'Zuzz'
    >>> fizzbuzz(21)
    'FizzZuzz'
    >>> fizzbuzz(35)
    'BuzzZuzz'
    >>> fizzbuzz(105)
    'FizzBuzzZuzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(1)
    '1'
    """
    return "".join(teilwort(n, teiler, wort) for teiler, wort in REGELN) or str(n)


def fizzbuzz_range(start: int = 1, end: int = 100) -> list[str]:
    """Rückt die FizzBuzz-Ergebnisse für den Bereich [start, end] zurück.

    >>> fizzbuzz_range(1, 7)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', 'Zuzz']
    """
    return [fizzbuzz(n) for n in range(start, end + 1)]


if __name__ == "__main__":
    for zeile in fizzbuzz_range():
        print(zeile)
