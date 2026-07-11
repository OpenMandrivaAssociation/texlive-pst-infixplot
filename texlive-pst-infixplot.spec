%global tl_name pst-infixplot
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11
Release:	%{tl_revision}.1
Summary:	Using PSTricks plotting capacities with infix expressions rather than RPN
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-infixplot
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-infixplot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-infixplot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Plotting functions with pst-plot is very powerful but sometimes
difficult to learn since the syntax of \psplot and \parametricplot
requires some PostScript knowledge. The infix-RPN and pst-infixplot
styles simplify the usage of pst-plot for the beginner, providing macro
commands that convert natural mathematical expressions to PostScript
syntax.

