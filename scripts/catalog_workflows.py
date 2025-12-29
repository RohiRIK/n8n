#!/usr/bin/env python3
import os, json, hashlib, argparse, datetime, sys

def sha1(path):
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def try_load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f), None
    except Exception as e:
        return None, str(e)

def extract_category(folder_path):
    """Extract category from folder path if it's in workflow_backups"""
    parts = folder_path.split(os.sep)
    if 'workflow_backups' in parts:
        idx = parts.index('workflow_backups')
        if len(parts) > idx + 1:
            return parts[idx + 1]
    return ""

def collect(root, rel_dirs):
    items = []
    now = datetime.datetime.utcnow().isoformat() + "Z"
    for rel in rel_dirs:
        base = os.path.join(root, rel)
        if not os.path.isdir(base):
            continue
        for dirpath, _, filenames in os.walk(base):
            for fn in filenames:
                if not fn.lower().endswith(".json"):
                    continue
                path = os.path.join(dirpath, fn)
                relpath = os.path.relpath(path, root)
                size = os.path.getsize(path)
                digest = sha1(path)
                data, err = try_load_json(path)
                folder_rel = os.path.relpath(dirpath, root)
                record = {
                    "path": relpath,
                    "folder": folder_rel,
                    "category": extract_category(folder_rel),
                    "file": fn,
                    "size_bytes": size,
                    "sha1": digest,
                    "cataloged_at": now,
                }
                if data:
                    record["name"] = data.get("name")
                    record["node_count"] = len(data.get("nodes", []))
                    tags = data.get("tags")
                    if isinstance(tags, list):
                        # n8n tags may be objects or strings
                        record["tags"] = [t.get("name") if isinstance(t, dict) else t for t in tags]
                else:
                    record["json_error"] = err
                items.append(record)
    return sorted(items, key=lambda x: x["path"])

def write_outputs(root, items):
    docs_dir = os.path.join(root, "docs")
    os.makedirs(docs_dir, exist_ok=True)
    json_out = os.path.join(docs_dir, "catalog.json")
    md_out = os.path.join(docs_dir, "catalog.md")
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    # Markdown table
    lines = []
    lines.append("# Workflow Catalog")
    lines.append("")
    lines.append("| Category | Path | Name | Nodes | Tags | Size | SHA1 |")
    lines.append("|---|---|---:|---:|---|---:|---|")
    for it in items:
        category = it.get('category', '')
        tags = ", ".join(it.get("tags", [])) if it.get("tags") else ""
        lines.append(f"| {category} | {it['path']} | {it.get('name','')} | {it.get('node_count','')} | {tags} | {it['size_bytes']} | {it['sha1'][:10]} |")
    with open(md_out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {json_out} and {md_out} with {len(items)} entries.")

def main():
    parser = argparse.ArgumentParser(description="Catalog n8n workflow JSON files.")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--dirs", default="workflow_backups,projects,development", help="Comma-separated directories to scan")
    args = parser.parse_args()
    rel_dirs = [d.strip() for d in args.dirs.split(",") if d.strip()]
    items = collect(args.root, rel_dirs)
    write_outputs(args.root, items)

if __name__ == "__main__":
    sys.exit(main())