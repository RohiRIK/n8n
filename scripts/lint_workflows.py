#!/usr/bin/env python3
import os, sys, json, argparse

def lint_file(path):
    problems = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "name" not in data or not data["name"]:
            problems.append("Missing or empty 'name'")
        if "nodes" not in data or not isinstance(data["nodes"], list):
            problems.append("Missing or invalid 'nodes' (expected list)")
    except Exception as e:
        problems.append(f"JSON parse error: {e}")
    return problems

def walk_and_lint(root, rel_dirs):
    had_issues = False
    for rel in rel_dirs:
        base = os.path.join(root, rel)
        if not os.path.isdir(base):
            continue
        for dirpath, _, filenames in os.walk(base):
            for fn in filenames:
                if not fn.lower().endswith(".json"):
                    continue
                p = os.path.join(dirpath, fn)
                probs = lint_file(p)
                if probs:
                    had_issues = True
                    print(f"[!] {os.path.relpath(p, root)}")
                    for pr in probs:
                        print(f"    - {pr}")
    return 1 if had_issues else 0

def main():
    parser = argparse.ArgumentParser(description="Lint n8n workflow JSON files.")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--dirs", default="development,projects", help="Comma-separated directories to scan")
    args = parser.parse_args()
    rel_dirs = [d.strip() for d in args.dirs.split(",") if d.strip()]
    sys.exit(walk_and_lint(args.root, rel_dirs))

if __name__ == "__main__":
    main()