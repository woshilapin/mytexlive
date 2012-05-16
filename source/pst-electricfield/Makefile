# $Id: Makefile 354 2010-06-18 17:18:01Z herbert $

# `Makefile' for `pst-electricfield.pdf', Rolf Niepraschk, 2010/05/21

.SUFFIXES : .tex .ltx .dvi .ps .pdf .eps .pro 

PACKAGE = pst-electricfield
MAIN = $(PACKAGE)-doc
LANGUAGES = DE EN FR
PRO = $(PACKAGE).pro


empty=
space=$(empty) $(empty)
DOC_SOURCES = $(addprefix $(PACKAGE)-doc,$(LANGUAGES)$(space))
DOC_SOURCES := $(addsuffix .tex, $(DOC_SOURCES))
DOCS = $(DOC_SOURCES:.tex=.pdf)

TDS = ~/PSTricks/PSTricks-TDS

LATEX  = pst2pdf 
PDFLATEX  = pdflatex 
OPTIONS= --Iext=.png --Iscale=0.5 --DPI=150 --noImages

ARCHNAME = $(PACKAGE)-$(shell date +%Y%m%d)

ARCHFILES = $(PACKAGE).sty $(PACKAGE).tex $(PACKAGE).pro $(DOC_SOURCES) \
  README Changes Makefile

all : $(DOCS) clean 

%.pdf : %.tex 
	$(LATEX) $(basename $<) $(OPTIONS)
#	makeindex -s gglo.ist -t $(basename $<)-pdf.glg -o $(basename $<)-pdf.gls $(basename $<)-pdf.glo
	makeindex -s pst-doc.ist -t $(basename $<)-pdf.ilg -o $(basename $<)-pdf.ind $(basename $<)-pdf.idx
	bibtex $(basename $<)-pdf
	$(PDFLATEX) $(basename $<)-pdf
	$(PDFLATEX) $(basename $<)-pdf
	mv $(basename $<)-pdf.pdf $(basename $<).pdf
	rm -f $(basename $<)-tmp.* $(basename $<)-pdf.* 

clean :
	$(RM) $(foreach i,$(DOC_SOURCES:.tex=),$(addprefix $i, \
          .log .plog .preamble .aux .glg .glo .gls .ilg .idx .ind .tmp .toc .out .blg .bbl))

veryclean : clean
	$(RM) $(foreach i,$(DOC_SOURCES:.tex=),$(addprefix $i, \
          .pdf .bbl .blg))

arch :
	zip $(ARCHNAME).zip $(ARCHFILES)

ifneq ($(strip $(PRO)),)
installPRO : 
	@echo "Installiere PRO-Dateien ($(PRO))..."
	cp -u Changes        $(TDS)/dvips/$(PACKAGE)/
	cp -u $(PACKAGE).pro $(TDS)/dvips/$(PACKAGE)/
	cp -u $(PACKAGE).pro ~/Links/dvips-local/
else
installPRO : 
	@:
endif

tds : installPRO
	@echo "Installiere TeX-Zeug..."
	cp -u Changes     $(TDS)/doc/generic/$(PACKAGE)/
	cp -u README      $(TDS)/doc/generic/$(PACKAGE)/
	cp -u *.pdf $(TDS)/doc/generic/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/tex/latex/$(PACKAGE)/
	cp -u $(PACKAGE).sty $(TDS)/tex/latex/$(PACKAGE)/
#
	cp -u Changes        $(TDS)/tex/generic/$(PACKAGE)/
	cp -u $(PACKAGE).tex $(TDS)/tex/generic/$(PACKAGE)/
#
	cp -u Changes     $(TDS)/source/$(PACKAGE)/
	cp -u *-doc??.tex $(TDS)/source/$(PACKAGE)/
	cp -u $(MAIN).bib $(TDS)/source/$(PACKAGE)/
	cp -u Makefile    $(TDS)/source/$(PACKAGE)/

debug :
	@echo $(DOC_SOURCES)

# EOF
