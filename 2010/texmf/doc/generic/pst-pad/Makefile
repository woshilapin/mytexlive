MAIN = pst-pad-doc
MAINDE = pst-pad-docDE

all: \
	$(MAIN).pdf \
	$(MAINDE).pdf

$(MAIN).pdf: \
	showexpl.cfg \
	pst-pad-doc.tex \
	pst-pad.tex \
	pst-pad.sty 
		latex $(MAIN).tex
		latex $(MAIN).tex
		dvips $(MAIN)
		ps2pdf $(MAIN).ps

$(MAINDE).pdf: \
	showexpl.cfg \
	pst-pad-docDE.tex \
	pst-pad.tex \
	pst-pad.sty 
		latex $(MAINDE).tex
		latex $(MAINDE).tex
		dvips $(MAINDE)
		ps2pdf $(MAINDE).ps

.PHONY: publish
publish: \
		all
		zip pst-pad.zip \
		pst-pad.tex pst-pad.sty showexpl.cfg Makefile README CHANGES \
		$(MAIN).tex $(MAIN).pdf \
		$(MAINDE).tex $(MAINDE).pdf

.PHONY: clean
clean:
		rm *~ *.aux *.backup *.bbl *.blg *.brf *.cb *.changes \
		*.dvi *.idx *.ilg *.ind *.inx *.lof *.log *.lot *.lox \
		*.out *.ps *.pdf *.rel *.tmp *.toc *.xcp *.zip
