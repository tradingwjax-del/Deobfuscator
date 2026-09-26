# Luau Deobfuscator

A Python deobfuscator for protected Roblox Luau scripts. It includes
`luau-ast` integration for parsing and rendering Luau and supports the
IronBrew 1 and Luraph v15 pipelines.

## iSH on iOS

iSH runs an x86 Alpine userspace, so its Luau executables need to be compiled
inside iSH. Do not copy a normal x86_64 Linux binary into iSH.

```sh
apk update
git clone https://github.com/tradingwjax-del/Deobfuscator.git
cd Deobfuscator
sh scripts/setup_ish.sh
```

Then put the input file in the repository directory and run:

```sh
python3 deobf.py -f leakd.lua
```

The full deobfuscation result is written to:

```text
output/leakd.lua
```

To choose another output path:

```sh
python3 deobf.py -f leakd.lua -o output/leakd-readable.lua
```

The `-f` form is a compatibility entrypoint for the requested iSH command;
full devirtualization is already the default mode. For a faster behaviour
trace without devirtualization, use:

```sh
python3 deobf.py -f leakd.lua --no-devirt
```

## Building Luau manually

The setup script invokes the repository's builder and creates both required
executables in `deobf/bin/`:

```sh
python3 deobf/build_luau.py --portable --no-lto --jobs 1
```

Increase `--jobs` only if the iSH process has enough memory. The generated
executables are platform-specific and should be rebuilt on each target
machine. The iSH setup uses dynamic linking and Unix Makefiles because
minimal Alpine installations may not provide everything required for static
linking, and Ninja can crash under iSH.