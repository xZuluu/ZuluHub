"""Seeker — criteria-based search over a local JSONL dataset."""
import sys
import json
import argparse


def emit(obj):
    print(json.dumps(obj), flush=True)


def _load(path):
    rows = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except Exception:
                    pass
    except Exception:
        pass
    return rows


def search(path, query, limit):
    q = (query or "").lower()
    hits = []
    for row in _load(path):
        blob = json.dumps(row, ensure_ascii=False).lower()
        if not q or q in blob:
            hits.append(row)
        if len(hits) >= limit:
            break
    return hits


def main(argv):
    ap = argparse.ArgumentParser(prog="seeker")
    ap.add_argument("--dataset", default="")
    ap.add_argument("--query", default="")
    ap.add_argument("--limit", type=int, default=50)
    a = ap.parse_args(argv)
    hits = search(a.dataset, a.query, a.limit)
    for h in hits:
        emit({"type": "row", "hit": h})
    emit({"type": "done", "count": len(hits)})


if __name__ == "__main__":
    main(sys.argv[1:])
