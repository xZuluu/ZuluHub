"""Email Generator — build address lists from a simple pattern.

Expands a pattern into email addresses across one or more domains.
Tokens: {word} = random letters, {num} = random digits.
"""
import sys
import json
import random
import string
import argparse


def emit(obj):
    print(json.dumps(obj), flush=True)


def _word(n):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def _num(n):
    return "".join(random.choice(string.digits) for _ in range(n))


def _expand(pattern):
    out = pattern or "{word}{num}"
    while "{word}" in out:
        out = out.replace("{word}", _word(random.randint(4, 8)), 1)
    while "{num}" in out:
        out = out.replace("{num}", _num(random.randint(2, 4)), 1)
    return out


def generate(pattern, count, domains):
    doms = domains or ["example.com"]
    return [f"{_expand(pattern)}@{random.choice(doms)}" for _ in range(count)]


def main(argv):
    ap = argparse.ArgumentParser(prog="email_generator")
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--pattern", default="{word}{num}")
    ap.add_argument("--domains", default="")
    a = ap.parse_args(argv)
    doms = [d.strip() for d in a.domains.split(",") if d.strip()]
    rows = generate(a.pattern, a.count, doms)
    for r in rows:
        emit({"type": "row", "email": r})
    emit({"type": "done", "count": len(rows)})


if __name__ == "__main__":
    main(sys.argv[1:])
