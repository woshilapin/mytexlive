# `Makefile' for `pst-slpe.pdf', hv, 2006/08/11

.SUFFIXES : .tex .ltx .dvi .ps .pdf .eps

PACKAGE = pst-slpe

LATEX = latex

MAIN = $(PACKAGE)-doc

TDS = ~/PSTricks/PSTricks-TDS

ARCHNAME = $(PACKAGE)-$(shell date +%y%m%d)

ARCHFILES = $(PACKAGE).dtx $(PACKAGE).ins Makefile

all : $(PACKAGE).sty doc clean

$(PACKAGE).sty : $(PACKAGE).dtx
%.sty : %.dtx
	tex $(basename $<).ins

doc: $(PACKAGE).pdf

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
	$(LATEX) $<

clean : 
	$(RM) $(addprefix $(PACKAGE), .log .aux .glg .glo .gls .ilg .idx .ind .tmp .toc .out)
	$(RM) $(addprefix $(PACKAGE), .dvi .ps)

veryclean : clean
	$(RM) $(PACKAGE).pdf
	$(RM) $(PACKAGE).pdf  $(addprefix $(PACKAGE), .tex .sty .pro)

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
	cp -u Changes        $(TDS)/dvips/$(PACKAGE)/
	cp -u $(PACKAGE).pro $(TDS)/dvips/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/source/$(PACKAGE)/
	cp -u $(PACKAGE).dtx $(TDS)/source/$(PACKAGE)/
	cp -u $(PACKAGE).ins $(TDS)/source/$(PACKAGE)/
	cp -u README         $(TDS)/source/$(PACKAGE)/
	cp -u Makefile       $(TDS)/source/$(PACKAGE)/

arch :
	zip $(ARCHNAME).zip $(ARCHFILES)

# EOF


