%global tl_name trfsigns
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Typeset transform signs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/trfsigns
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trfsigns.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for typesetting various transformation signs for Laplace
transforms, Fourier transforms and others.

