# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/trfsigns
# catalog-date 2006-12-05 00:47:24 +0100
# catalog-license gpl
# catalog-version 1.01
Name:		texlive-trfsigns
Version:	1.01
Release:	2
Summary:	Typeset transform signs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/trfsigns
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
