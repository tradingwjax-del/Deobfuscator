#!/usr/bin/env python3
"""Compatibility CLI: python3 deobf.py -f INPUT [options].

The underlying deobfuscator uses a positional input and full devirtualization
by default. The -f flag is accepted here as an explicit full-mode alias.
"""
import os
import sys


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
    sys.argv = [os.path.join(os.path.dirname(__file__), "deob.py")] + forwarded

    from deob import main as run_deobfuscator
    run_deobfuscator()


if __name__ == "__main__":
    main()
