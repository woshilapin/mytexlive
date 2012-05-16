# `Makefile' for `pst2pdf.pdf', hv, 2006/08/11

.SUFFIXES : .tex .ltx .dvi .ps .pdf .eps

PACKAGE = pst2pdf

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
	$(RM) $(addprefix $(MAIN), .log .aux .glg .glo .gls .ilg .idx .ind .tmp .toc .out )
	$(RM) $(addprefix $(MAIN), .dvi .ps)

veryclean : clean
	$(RM) $(addprefix $(MAIN), .pdf .bbl .blg)

arch :
	zip $(ARCHNAME).zip $(ARCHFILES)

tds:
	cp -u Changes     $(TDS)/scripts/$(PACKAGE)/
	cp -u README      $(TDS)/scripts/$(PACKAGE)/
	cp -u $(MAIN).pdf $(TDS)/scripts/$(PACKAGE)/
	cp -u $(MAIN).tex $(TDS)/scripts/$(PACKAGE)/
	cp -u $(MAIN).bib $(TDS)/scripts/$(PACKAGE)/
	cp -u Makefile    $(TDS)/scripts/$(PACKAGE)/
	cp -u test?.tex   $(TDS)/scripts/$(PACKAGE)/
	cp -u test?-pdf.pdf   $(TDS)/scripts/$(PACKAGE)/
	cp -u pst2pdf.pl  $(TDS)/scripts/$(PACKAGE)/


# EOF
