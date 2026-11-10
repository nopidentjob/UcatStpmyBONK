"""Переводит температуру между градусами Цельсия и Фаренгейта.

Примеры:
    python converter.py 20 c   ->  20.0 C = 68.0 F
    python converter.py 68 f   ->  68.0 F = 20.0 C
"""
import sys


def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[2].lower() not in ("c", "f"):
        sys.exit("Использование: python converter.py число c|f")
    value = float(sys.argv[1])
    if sys.argv[2].lower() == "c":
        print(f"{value} C = {c_to_f(value):.1f} F")
    else:
        print(f"{value} F = {f_to_c(value):.1f} C")
