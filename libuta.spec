Summary:	libuta - a C++ multimedia framework
Summary(pl):	libuta - ¶rodowisko multimedialne do C++
Name:		libuta
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Libraries
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
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libuta is C++ library which provides a framework for creating
multimedia applications, especially games. It runs on top of SDL and
is available for Win32 and Linux/X11.

%description -l pl
libuta jest bibliotek± C++ daj±c± ¶rodowisko do tworzenia aplikacji
multimedialnych, zw³aszcza gier. Opiera siê na SDL i jest dostêpna pod
Win32 i Linuksa/X11.

%package devel
Summary:	Header files for libuta development
Summary(pl):	Pliki nag³ówkowe do tworzenia programów z u¿yciem libuta
Group:		Development/Libraries
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

%description -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do tworzenia programów z
u¿yciem biblioteki libuta.

%package static
Summary:	Static libraries for libuta development
Summary(pl):	Statyczne biblioteki libuta
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libuta is C++ library which provides a framework for creating
multimedia applications, especially games. It runs on top of SDL and
is available for Win32 and Linux/X11.

This package contains the static libuta.

%description static -l pl
Ten pakiet zawiera statyczn± bibliotekê libuta.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoheader
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
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
