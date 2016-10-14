# Introduction
This repository is a bunch of various LaTeX packages.  Since this is only the
sources, you have to build them and put them at the right place in order to use
them.

# Installation
First, clone the repository where LaTeX will see it.  On Linux, you can usually
do the following (`~/texmf` folder is read in most default configurations of
LaTeX).

```
git clone https://github.com/woshilapin/mytexlive.git ~/texmf
```

Then you'll have to build the packages.

```
cd ~/texmf/tex/latex
python3 update.py
```
