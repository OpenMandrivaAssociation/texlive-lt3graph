# revision 32356
# category Package
# catalog-ctan /macros/latex/contrib/lt3graph
# catalog-date 2013-12-08 00:11:37 +0100
# catalog-license lppl1.3
# catalog-version 0.0.9-r1
Name:		texlive-lt3graph
Version:	0.0.9.r1
Release:	1
Summary:	Provide a graph datastructure for experimental LaTeX3
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lt3graph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3graph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3graph.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a 'graph' data structure, for use in
documents that are using the experimental LaTeX 3 syntax.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lt3graph/lt3graph-dry.sty
%{_texmfdistdir}/tex/latex/lt3graph/lt3graph-packagedoc.cls
%{_texmfdistdir}/tex/latex/lt3graph/lt3graph.sty
%doc %{_texmfdistdir}/doc/latex/lt3graph/README
%doc %{_texmfdistdir}/doc/latex/lt3graph/lt3graph.pdf
%doc %{_texmfdistdir}/doc/latex/lt3graph/lt3graph.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
