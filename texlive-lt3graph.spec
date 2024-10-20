Name:		texlive-lt3graph
Version:	45913
Release:	2
Summary:	Provide a graph datastructure for experimental LaTeX3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lt3graph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3graph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3graph.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/lt3graph
%doc %{_texmfdistdir}/doc/latex/lt3graph

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
