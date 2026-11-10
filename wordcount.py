"""Считает строки, слова и символы в текстовом файле.

Запуск: python wordcount.py имя_файла.txt
"""
import sys


def count(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return len(text.splitlines()), len(text.split()), len(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Использование: python wordcount.py имя_файла.txt")
    lines, words, chars = count(sys.argv[1])
    print(f"Строк: {lines}, слов: {words}, символов: {chars}")
