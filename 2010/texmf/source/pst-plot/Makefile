
# `Makefile' for `pst-plot-doc.pdf', hv, 2010/01/22

.SUFFIXES : .tex .ltx .dvi .ps .pdf .eps

PACKAGE = pst-plot

MAIN = $(PACKAGE)-doc

LATEX = latex

ARCHNAME = $(MAIN)-$(shell date +%y%m%d)

ARCHFILES = $(PACKAGE).sty $(PACKAGE).tex $(PACKAGE).pro $(MAIN).tex README Changes Makefile

TDS = ~/PSTricks/PSTricks-TDS

all : doc clean 
#tds

doc: $(MAIN).pdf

$(MAIN).pdf : $(MAIN).ps
	GS_OPTIONS="-dAutoRotatePages=/None -dNoSafer" ps2pdf $<
#	echo "\documentclass[a4paper]{article}" > temp.tex
#	echo "\usepackage{pdfpages}" >> temp.tex
#	echo "\begin{document}" >> temp.tex
#	echo "\includepdf[pages=1-5]{pst-plot-doc}" >> temp.tex
#	echo "\includepdf[pages=25-29]{../pstricks/doc/pstricks-doc}" >> temp.tex
#	echo "\includepdf[pages=6-]{pst-plot-doc}" >> temp.tex
#	echo "\end{document}" >> temp.tex
#	pdflatex temp
#	mv temp.pdf pst-plot-doc.pdf

$(MAIN).ps : $(MAIN).dvi
	dvips $<

$(MAIN).dvi : $(MAIN).tex
	$(LATEX) $<
	$(LATEX) $<
	if ! test -f $(basename $<).glo ; then touch $(basename $<).glo; fi
	if ! test -f $(basename $<).idx ; then touch $(basename $<).idx; fi
	makeindex -s gglo.ist -t $(basename $<).glg -o $(basename $<).gls \
	  $(basename $<).glo
	makeindex -s pst-doc.ist -t $(basename $<).ilg -o $(basename $<).ind \
	  $(basename $<).idx
	bibtex $(basename $<)
	$(LATEX) $<
	$(LATEX) $<

clean : 
	$(RM) $(addprefix $(MAIN), .log .aux .glg .glo .gls .ilg .idx .ind .tmp .toc .out )
	$(RM) $(addprefix $(MAIN), .dvi .ps .blg .bbl )
	rm *.data
#	rm temp*

veryclean : clean
	$(RM) $(addprefix $(MAIN), .pdf .bbl .blg)

arch :
	zip $(ARCHNAME).zip $(ARCHFILES)

tds:
	cp -u *.sty ~/Links/texmf-local-latex/$(PACKAGE)/
#
	cp -u Changes     $(TDS)/doc/generic/$(PACKAGE)/
	cp -u README      $(TDS)/doc/generic/$(PACKAGE)/
	cp -u $(MAIN).pdf $(TDS)/doc/generic/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/tex/latex/$(PACKAGE)/
	cp -u $(PACKAGE).sty $(TDS)/tex/latex/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/tex/generic/$(PACKAGE)/
	cp -u $(PACKAGE).tex $(TDS)/tex/generic/$(PACKAGE)/
	cp -u $(PACKAGE)97.tex $(TDS)/tex/generic/$(PACKAGE)/
#
#	cp -u Changes        $(TDS)/dvips/$(PACKAGE)/
#	cp -u $(PACKAGE).pro $(TDS)/dvips/$(PACKAGE)/
#
	cp -u Changes     $(TDS)/source/$(PACKAGE)/
	cp -u $(MAIN).tex $(TDS)/source/$(PACKAGE)/
	cp -u $(MAIN).bib $(TDS)/source/$(PACKAGE)/
	cp -u Makefile    $(TDS)/source/$(PACKAGE)/


# EOF
