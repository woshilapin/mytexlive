# `Makefile' for `pst-news.pdf', hv, 2007/03/17

.SUFFIXES : .tex .ltx .dvi .ps .pdf .eps

PACKAGE = pst-news$(shell date +%y)

MAIN = $(PACKAGE)

BASE = pstricks

LATEX = latex

TDS = ~/PSTricks/PSTricks-TDS

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

tds:
#################### base #########################
	cp -u ../config/*        ../.base/config/
#
	cp -u Changes            ../.base/doc/
	cp -u pst-doc.*          ../.base/doc/
	cp -u PSTricks.bib*      ../.base/doc/
	cp -u pst-news*          ../.base/doc/
	cp -u pst-user*          ../.base/doc/
	cp -u *.sty              ../.base/doc/
	cp -u pstricks-*         ../.base/doc/
	cp -u test*              ../.base/doc/
	cp -u images/*           ../.base/doc/images/
#
	cp -u ../dvips/*         ../.base/dvips/
	cp -u ../generic/*       ../.base/generic/
	cp -u ../latex/*         ../.base/latex/
	cp -u ../README          ../.base/
#
#################### TDS #########################
	cp -u Changes     $(TDS)/doc/generic/$(BASE)/
	cp -u README      $(TDS)/doc/generic/$(BASE)/
	cp -u $(MAIN).pdf $(TDS)/doc/generic/$(BASE)/
#
	cp -u ../latex/Changes        $(TDS)/tex/latex/$(BASE)/
	cp -u ../latex/$(BASE).sty $(TDS)/tex/latex/$(BASE)/
#
	cp -u ../generic/Changes        $(TDS)/tex/generic/$(BASE)/
	cp -u ../generic/$(BASE).tex $(TDS)/tex/generic/$(BASE)/
#
	cp -u ../dvips/Changes        $(TDS)/dvips/$(BASE)/
#	cp -u ../dvips/$(BASE).pro $(TDS)/dvips/$(BASE)/
#	cp -u ../dvips/$(BASE)97.pro $(TDS)/dvips/$(BASE)/
	cp -u ../dvips/*.pro $(TDS)/dvips/$(BASE)/
#
	cp -u Changes     $(TDS)/source/$(BASE)/
	cp -u $(MAIN).tex $(TDS)/source/$(BASE)/
#	cp -u $(MAIN).bib $(TDS)/source/$(BASE)/
	cp -u Makefile    $(TDS)/source/$(BASE)/

# EOF
