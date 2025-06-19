#!/usr/bin/env python3
"""
Hackerrank – Camel Case (#strings > split/combine)

Lê linhas no formato OP;TIPO;TEXTO e:
  • OP=="S":  divide camelCase/PascalCase em palavras minúsculas.
  • OP=="C":  combina palavras em camelCase, PascalCase ou método().
"""

import re
import sys
from typing import List

_SPLIT_RE = re.compile(r"(?<!^)(?=[A-Z])")


def _split_camel(value: str) -> str:
    """Converte camelCase / PascalCase (/Method()) em 'palavras separadas'."""
    value = value.rstrip("()\n")
    parts = _SPLIT_RE.split(value)
    return " ".join(p.lower() for p in parts)


def _combine(words: str, kind: str) -> str:
    """Une palavras separadas em camelCase, PascalCase ou método()."""
    tokens: List[str] = words.lower().split()
    if kind == "C":
        out = "".join(t.title() for t in tokens)
    else:
        out = tokens[0] + "".join(t.title() for t in tokens[1:])
        if kind == "M":
            out += "()"
    return out


def main() -> None:
    for raw in sys.stdin:
        op, kind, value = raw.strip().split(";")
        if op == "S":
            sys.stdout.write(_split_camel(value) + "\n")
        elif op == "C":
            sys.stdout.write(_combine(value, kind) + "\n")


if __name__ == "__main__":
    main()
