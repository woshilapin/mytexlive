
# `Makefile' for `pst-blur.pdf', RN, 2005/10/07

.SUFFIXES : .tex .ltx .dvi .ps .pdf .eps

PACKAGE = pst-blur

LATEX = latex

ARCHNAME = $(PACKAGE)-$(shell date +%y%m%d)

ARCHFILES = $(PACKAGE).dtx $(PACKAGE).ins Makefile

TDS = ~/PSTricks/PSTricks-TDS

all : sty doc 
sty : 
	tex $(PACKAGE).ins

doc : $(PACKAGE).pdf

$(PACKAGE).pdf : $(PACKAGE).ps
	GS_OPTIONS=-dAutoRotatePages=/None ps2pdf $<

$(PACKAGE).ps : $(PACKAGE).dvi
	dvips $<

$(PACKAGE).dvi : $(PACKAGE).dtx
	$(LATEX) $<
	if ! test -f $(basename $<).glo ; then touch $(basename $<).glo; fi
	if ! test -f $(basename $<).idx ; then touch $(basename $<).idx; fi
	makeindex -s gglo.ist -t $(basename $<).glg -o $(basename $<).gls \
	  $(basename $<).glo
	makeindex -s gind.ist -t $(basename $<).ilg -o $(basename $<).ind \
	  $(basename $<).idx
	$(LATEX) $<

clean : 
	$(RM) $(addprefix $(PACKAGE), .log .aux .glg .glo .gls .ilg .idx .ind)
	$(RM) $(addprefix $(PACKAGE), .dvi .ps)

veryclean : clean
	$(RM) $(PACKAGE).pdf

arch :
	zip $(ARCHNAME).zip $(ARCHFILES)

tds:
	cp -u Changes     $(TDS)/doc/generic/$(PACKAGE)/
	cp -u README      $(TDS)/doc/generic/$(PACKAGE)/
	cp -u $(PACKAGE).pdf $(TDS)/doc/generic/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/tex/latex/$(PACKAGE)/
	cp -u $(PACKAGE).sty $(TDS)/tex/latex/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/tex/generic/$(PACKAGE)/
	cp -u $(PACKAGE).tex $(TDS)/tex/generic/$(PACKAGE)/
#
#	cp -u Changes        $(TDS)/dvips/$(PACKAGE)/
#	cp -u $(PACKAGE).pro $(TDS)/dvips/$(PACKAGE)/
#
	cp -u Changes     $(TDS)/source/$(PACKAGE)/
	cp -u $(PACKAGE).dtx $(TDS)/source/$(PACKAGE)/
	cp -u $(PACKAGE).ins $(TDS)/source/$(PACKAGE)/
	cp -u Makefile    $(TDS)/source/$(PACKAGE)/
# EOF
