"""Email Cleaner — validate, dedupe and normalize an address list."""
import sys
import re
import json
import argparse

_ADDR = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def emit(obj):
    print(json.dumps(obj), flush=True)


def clean(lines):
    seen = set()
    out = []
    for ln in lines:
        a = ln.strip().lower()
        if not a or a in seen:
            continue
        seen.add(a)
        if _ADDR.match(a):
            out.append(a)
    return out


def main(argv):
    ap = argparse.ArgumentParser(prog="email_cleaner")
    ap.add_argument("--input", default="")
    a = ap.parse_args(argv)
    try:
        with open(a.input, encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        lines = []
    rows = clean(lines)
    for r in rows:
        emit({"type": "row", "email": r})
    emit({"type": "done", "kept": len(rows)})


if __name__ == "__main__":
    main(sys.argv[1:])
