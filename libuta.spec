Summary:	libuta - a C++ multimedia framework
Name:		libuta
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://victor.worldforge.org/pub/worldforge/libs/libuta/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	Atlas-C++-devel
BuildRequires:	varconf-devel
BuildRequires:	smpeg-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libpng-devel
BuildRequires:	freetype1-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libuta is C++ library which provides a framework for creating
multimedia applications, especially games. It runs on top of SDL and
is available for Win32 and Linux/X11.

%package devel
Summary:	Header files and libraries for libuta development
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}
Requires:	Atlas-C++-devel
Requires:	varconf-devel
Requires:	smpeg-devel
Requires:	SDL_mixer-devel
Requires:	libpng-devel
Requires:	freetype1-devel

%description devel
libuta is C++ library which provides a framework for creating
multimedia applications, especially games. It runs on top of SDL and
is available for Win32 and Linux/X11.

This package contains the header files needed to develop programs that
use these libuta.

%package static
Summary:	Static libraries for libuta development
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
libuta is C++ library which provides a framework for creating
multimedia applications, especially games. It runs on top of SDL and
is available for Win32 and Linux/X11.

This package contains the static libuta.

%prep
%setup -q

%build
aclocal
autoheader
libtoolize --automake --copy --force
automake --add-missing --copy --gnu --force
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/lib*.so.0
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uta-config
%{_includedir}/uta
%attr(755,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_aclocaldir}/uta.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
