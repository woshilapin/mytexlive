# `Makefile' for `pst-light3d.pdf', hv, 2008/08/11

.SUFFIXES : .tex .ltx .dvi .ps .pdf .eps

PACKAGE = pst-light3d

MAIN = $(PACKAGE)-doc

LATEX = latex

TDS = ~/PSTricks/PSTricks-TDS

ARCHNAME = $(MAIN)-$(shell date +%y%m%d)

ARCHFILES = $(PACKAGE).sty $(PACKAGE).tex $(PACKAGE).pro $(MAIN).tex README Changes Makefile

all : doc clean tds

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
	$(RM) $(addprefix $(MAIN), .log .aux .glg .glo .gls .ilg .idx .ind .tmp .toc .out )
	$(RM) $(addprefix $(MAIN), .dvi .ps)

veryclean : clean
	$(RM) $(addprefix $(MAIN), .pdf .bbl .blg)

tds:
	cp -u Changes     $(TDS)/doc/generic/$(PACKAGE)/
	cp -u README      $(TDS)/doc/generic/$(PACKAGE)/
	cp -u $(MAIN).pdf $(TDS)/doc/generic/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/tex/latex/$(PACKAGE)/
	cp -u $(PACKAGE).sty $(TDS)/tex/latex/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/tex/generic/$(PACKAGE)/
	cp -u $(PACKAGE).tex $(TDS)/tex/generic/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/dvips/$(PACKAGE)/
	cp -u $(PACKAGE).pro $(TDS)/dvips/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/source/$(PACKAGE)/
	cp -u README         $(TDS)/source/$(PACKAGE)/
	cp -u Makefile       $(TDS)/source/$(PACKAGE)/
	cp -u $(MAIN).tex $(TDS)/tex/generic/$(PACKAGE)/
	cp -u $(MAIN).bib $(TDS)/tex/generic/$(PACKAGE)/

arch :
	zip $(ARCHNAME).zip $(ARCHFILES)

# EOF
