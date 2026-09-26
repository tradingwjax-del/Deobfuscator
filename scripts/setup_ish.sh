#!/bin/sh
# Install the native Luau tools required by the deobfuscator in iSH.
#
# iSH is an x86 Alpine userspace on iOS. The Luau executables must therefore
# be compiled inside iSH instead of copying an x86_64 Linux binary from a
# desktop or a release archive.
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"

if ! command -v apk >/dev/null 2>&1; then
    echo "This setup script is for iSH's Alpine userspace (apk)." >&2
    exit 1
fi

echo "[*] installing iSH build dependencies"
apk add --no-cache ca-certificates cmake g++ git make python3

echo "[*] building luau and luau-ast (low-memory iSH build)"
python3 deobf/build_luau.py --portable --no-lto --jobs "${DEOBF_BUILD_JOBS:-1}"

chmod 755 deobf/bin/luau deobf/bin/luau-ast
echo "[+] ready: deobf/bin/luau"
echo "[+] ready: deobf/bin/luau-ast"
echo
echo "Run from this directory:"
echo "  python3 deobf.py -f leakd.lua"
echo
echo "The default result is:"
echo "  output/leakd.lua"