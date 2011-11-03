# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/trfsigns
# catalog-date 2006-12-05 00:47:24 +0100
# catalog-license gpl
# catalog-version 1.01
Name:		texlive-trfsigns
Version:	1.01
Release:	1
Summary:	Typeset transform signs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/trfsigns
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package for typesetting various transformation signs for
Laplace transforms, Fourier transforms and others.

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
%{_texmfdistdir}/tex/latex/trfsigns/trfsigns.sty
%doc %{_texmfdistdir}/doc/latex/trfsigns/COPYING
%doc %{_texmfdistdir}/doc/latex/trfsigns/README
%doc %{_texmfdistdir}/doc/latex/trfsigns/trfexamp.tex
%doc %{_texmfdistdir}/doc/latex/trfsigns/trfsigns.pdf
#- source
%doc %{_texmfdistdir}/source/latex/trfsigns/trfsigns.drv
%doc %{_texmfdistdir}/source/latex/trfsigns/trfsigns.dtx
%doc %{_texmfdistdir}/source/latex/trfsigns/trfsigns.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
