# `Makefile' for `pst-map3d-doc.pdf', hv, 2008/08/26

.SUFFIXES : .tex .dvi .ps .pdf .eps

PACKAGE = pst-map2d
PACKTDS = pst-geo

MAIN = $(PACKAGE)-doc

LATEX = latex

ARCHNAME = $(MAIN)-$(shell date +%y%m%d)

ARCHFILES = $(PACKAGE).sty $(PACKAGE).tex $(PACKAGE).pro $(MAIN).tex README Changes Makefile

TDS = ~/PSTricks/PSTricks-TDS

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
	$(RM) *.dat
	$(RM) $(addprefix $(MAIN), .log .aux .bbl .blg .glg .glo .gls .ilg .idx .ind .tmp .toc .out )
	$(RM) $(addprefix $(MAIN), .dvi .ps)

veryclean : clean
	$(RM) $(addprefix $(MAIN), .pdf )

arch :
	zip $(ARCHNAME).zip $(ARCHFILES)

tds:
	cp -u ../Changes     $(TDS)/doc/generic/$(PACKTDS)/
	cp -u ../README      $(TDS)/doc/generic/$(PACKTDS)/
	cp -u *.pdf $(TDS)/doc/generic/$(PACKTDS)/
#
	cp -u ../Changes        $(TDS)/tex/latex/$(PACKTDS)/
	cp -u ../*.sty $(TDS)/tex/latex/$(PACKTDS)/
#
	cp -u ../Changes        $(TDS)/tex/generic/$(PACKTDS)/
	cp -u ../*.tex $(TDS)/tex/generic/$(PACKTDS)/
#
	cp -u ../Changes        $(TDS)/dvips/$(PACKTDS)/
	cp -u ../*.pro $(TDS)/dvips/$(PACKTDS)/
#
	cp -u ../Changes     $(TDS)/source/$(PACKTDS)/
	cp -u *.tex $(TDS)/source/$(PACKTDS)/
	cp -u *.bib $(TDS)/source/$(PACKTDS)/
	cp -u Makefile    $(TDS)/source/$(PACKTDS)/

# EOF
