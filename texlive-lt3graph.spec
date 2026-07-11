%global tl_name lt3graph
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.9
Release:	%{tl_revision}.1
Summary:	Provide a graph datastructure for experimental LaTeX3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lt3graph
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3graph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3graph.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a 'graph' data structure, for use in documents that
are using the experimental LaTeX 3 syntax.

