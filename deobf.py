#!/usr/bin/env python3
"""Run the deobfuscator from the repository root.

Examples:
    python3 deobf.py -f leakd.lua
    python3 deobf.py -f leakd.lua -o output/leakd-readable.lua

The compatibility wrapper in deobf/deobf.py keeps ``-f`` as the explicit
full-deobfuscation input form requested by the iSH workflow.
"""
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
DEOBF_DIR = os.path.join(HERE, "deobf")
if DEOBF_DIR not in sys.path:
    sys.path.insert(0, DEOBF_DIR)


def main():
    args = sys.argv[1:]
    if "-f" not in args:
        print("usage: python3 deobf.py -f INPUT [options]", file=sys.stderr)
        print("full deobfuscation is the default; -f is required by this wrapper", file=sys.stderr)
        raise SystemExit(2)

    flag = args.index("-f")
    if flag + 1 >= len(args) or args[flag + 1].startswith("-"):
        print("deobf.py: -f requires an input .lua/.luau file", file=sys.stderr)
        raise SystemExit(2)

    input_path = args[flag + 1]
    forwarded = args[:flag] + [input_path] + args[flag + 2:]
    sys.argv = [os.path.join(DEOBF_DIR, "deob.py")] + forwarded

    from deob import main as run_deobfuscator
    run_deobfuscator()


if __name__ == "__main__":
    main()