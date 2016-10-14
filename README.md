# Introduction
This repository is a bunch of various LaTeX packages.  Since this is only the
sources, you have to build them and put them at the right place in order to use
them.

# Build
First, clone the repository (you may want to look next section first for where
to clone it).  Then you'll have to build the packages.

```
cd ~/texmf/tex/latex
python3 update.py
```

Note, some of the packages need other of the packages to be built.  So you might
want to install first (see below) then try to build.  At the end, you'll
probably need a last update of the LaTeX packages database (`texhash` or
`initexmf --update-fndb`).

# Installation
You have 2 ways of installing the packages.
## Installation in `texmf`
You can clone the repository directly where LaTeX will see it.  On Linux, you can usually
do the following (`~/texmf` folder is read in most default configurations of
LaTeX).

```
git clone https://github.com/woshilapin/mytexlive.git ~/texmf
```

If on Windows or want another folder to be used, you can take a look into the
file `web2c/texmf.cnf` from your LaTeX installation and look or change the
variable `TEXMFHOME`.

Then finally, reconstruct the index.

```
texhash
```

# Installation with `inittexmf`
You might also clone the repository anywhere you want and use the following
command.

```
initexmf --register-root=/the/path/to/your/clone
initexmf --update-fndb
```
