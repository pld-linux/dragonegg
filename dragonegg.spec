Summary:	DragonEgg - using LLVM as a GCC backend
Summary(pl.UTF-8):	DragonEgg - użycie LLVM-a jako backendu GCC
Name:		dragonegg
Version:	3.6.0
Release:	0.1
License:	GPL v2+
Group:		Development/Tools
#Source0Download: http://llvm.org/releases/download.html
Source0:	http://llvm.org/releases/%{version}/dragonegg-%{version}.src.tar.xz
# Source0-md5:	bcc695c9515353a0a91f27b496bc2047
URL:		http://dragonegg.llvm.org/
# gcc plugin headers
BuildRequires:	gcc >= 6:4.5
BuildRequires:	gcc < 6:4.9
BuildRequires:	llvm-devel >= 3.5.1
# FIXME: https://llvm.org/bugs/show_bug.cgi?id=22925
BuildRequires:	llvm-devel < 3.6.0
Requires:	gcc >= 6:4.5
Requires:	llvm >= 3.5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DragonEgg is a gcc plugin that replaces GCC's optimizers and code
generators with those from the LLVM project. It works with gcc-4.5 or
newer, can target the x86/x86_64 and ARM processor families, and has
been successfully used on the Darwin, FreeBSD, kFreeBSD, Linux and
OpenBSD platforms. It fully supports Ada, C, C++ and Fortran. It has
partial support for Go, Java, Obj-C and Obj-C++.

%description -l pl.UTF-8
DragonEgg ("smocze jajo") to wtyczka gcc zastępująca optymalizatory i
generatory kodu GCC tymi z projektu LLVM. Działa z gcc 4.5 i nowszymi,
potrafi generować kod na procesory x86/x86_64 oraz ARM, działa na
platformach Darwin, FreeBSD, kFreeBSD, Linux oraz OpenBSD. Obsługuje w
pełni języki Ada, C, C++ i Fortran, natomiast częściowo - Go, Java,
Obj-C oraz Obj-C++.

%prep
%setup -q -n dragonegg-%{version}.src

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
CPPFLAGS="%{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/dragonegg

install dragonegg.so $RPM_BUILD_ROOT%{_libdir}/dragonegg
cp -p integrated-as.specs $RPM_BUILD_ROOT%{_libdir}/dragonegg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%dir %{_libdir}/dragonegg
%attr(755,root,root) %{_libdir}/dragonegg/dragonegg.so
%{_libdir}/dragonegg/integrated-as.specs
