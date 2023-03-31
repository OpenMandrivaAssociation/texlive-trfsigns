Name:		texlive-trfsigns
Version:	15878
Release:	2
Summary:	Typeset transform signs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/trfsigns
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for typesetting various transformation signs for
Laplace transforms, Fourier transforms and others.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/trfsigns/trfsigns.sty
%doc %{_texmfdistdir}/doc/latex/trfsigns/COPYING
%doc %{_texmfdistdir}/doc/latex/trfsigns/README
%doc %{_texmfdistdir}/doc/latex/trfsigns/trfexamp.tex
%doc %{_texmfdistdir}/doc/latex/trfsigns/trfsigns.pdf
#- source
%doc %{_texmfdistdir}/source/latex/trfsigns/trfsigns.drv
%doc %{_texmfdistdir}/source/latex/trfsigns/trfsigns.dtx
%doc %{_texmfdistdir}/source/latex/trfsigns/trfsigns.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
