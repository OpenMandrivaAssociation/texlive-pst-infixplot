# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-infixplot
# catalog-date 2006-12-19 19:38:44 +0100
# catalog-license lppl
# catalog-version 0.11
Name:		texlive-pst-infixplot
Version:	0.11
Release:	1
Summary:	Using pstricks plotting capacities with infix expressions rather than RPN
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-infixplot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-infixplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-infixplot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Plotting functions with pst-plot is very powerful but sometimes
difficult to learn since the syntax of \psplot and
\parametricplot requires some PostScript knowledge. The infix-
RPN and pst-infixplot styles simplify the usage of pst-plot for
the beginner, providing macro commands that convert natural
mathematical expressions to PostScript syntax.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-infixplot/infix-RPN.tex
%{_texmfdistdir}/tex/generic/pst-infixplot/pst-infixplot.tex
%{_texmfdistdir}/tex/latex/pst-infixplot/infix-RPN.sty
%{_texmfdistdir}/tex/latex/pst-infixplot/pst-infixplot.sty
%doc %{_texmfdistdir}/doc/generic/pst-infixplot/README
%doc %{_texmfdistdir}/doc/generic/pst-infixplot/pst-infixplot-doc.ps
%doc %{_texmfdistdir}/doc/generic/pst-infixplot/pst-infixplot-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-infixplot/pst-infixplot.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
