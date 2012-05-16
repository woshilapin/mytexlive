
# `Makefile' for `pst-3dplot.pdf', hv, 2007/03/17

.SUFFIXES : .tex .ltx .dvi .ps .pdf .eps

PACKAGE = pst-3dplot

MAIN = $(PACKAGE)-doc

LATEX = latex

ARCHNAME = $(MAIN)-$(shell date +%y%m%d)

ARCHFILES = $(PACKAGE).sty $(PACKAGE).tex $(PACKAGE).pro $(MAIN).tex README Changes Makefile

all : doc clean
doc: $(MAIN).pdf

$(MAIN).pdf : $(MAIN).ps
	GS_OPTIONS=-dAutoRotatePages=/None ps2pdf $<

$(MAIN).ps : $(MAIN).dvi
	dvips $<

$(MAIN).dvi : $(MAIN).tex
	$(LATEX) $<
	$(LATEX) $<
	if ! test -f $(basename $<).glo ; then touch $(basename $<).glo; fi
	if ! test -f $(basename $<).idx ; then touch $(basename $<).idx; fi
	makeindex -s gglo.ist -t $(basename $<).glg -o $(basename $<).gls \
	  $(basename $<).glo
	makeindex -t $(basename $<).ilg -o $(basename $<).ind \
	  $(basename $<).idx
	bibtex $(basename $<)
	$(LATEX) $<
	$(LATEX) $<

clean : 
	$(RM) $(addprefix $(MAIN), .log .aux .glg .glo .gls .ilg .idx .ind .tmp .toc .out .blg .Roessler .bbl )
	$(RM) $(addprefix $(MAIN), .dvi .ps)

veryclean : clean
	$(RM) $(addprefix $(MAIN), .pdf .bbl .blg)

arch :
	zip $(ARCHNAME).zip $(ARCHFILES)

# EOF
