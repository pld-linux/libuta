Summary:	libuta - a C++ multimedia framework
Summary(pl.UTF-8):	libuta - środowisko multimedialne do C++
Name:		libuta
Version:	0.4.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://victor.worldforge.org/pub/worldforge/libs/libuta/%{name}-%{version}.tar.gz
# Source0-md5:	06607ef03d84d607d4a1a1592f815eaf
Patch0:		%{name}-missing_assert_h.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	smpeg-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libpng-devel
BuildRequires:	freetype1-devel
BuildRequires:	libsigc++1-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libuta is C++ library which provides a framework for creating
multimedia applications, especially games. It runs on top of SDL and
is available for Win32 and Linux/X11.

%description -l pl.UTF-8
libuta jest biblioteką C++ dającą środowisko do tworzenia aplikacji
multimedialnych, zwłaszcza gier. Opiera się na SDL i jest dostępna pod
Win32 i Linuksa/X11.

%package devel
Summary:	Header files for libuta development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów z użyciem libuta
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	smpeg-devel
Requires:	SDL_mixer-devel
Requires:	libpng-devel
Requires:	freetype1-devel
Requires:	libsigc++1-devel

%description devel
libuta is C++ library which provides a framework for creating
multimedia applications, especially games. It runs on top of SDL and
is available for Win32 and Linux/X11.

This package contains the header files needed to develop programs that
use these libuta.

%description devel -l pl.UTF-8
libuta jest biblioteką C++ dającą środowisko do tworzenia aplikacji
multimedialnych, zwłaszcza gier. Opiera się na SDL i jest dostępna pod
Win32 i Linuksa/X11.

Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów z
użyciem biblioteki libuta.

%package static
Summary:	Static libraries for libuta development
Summary(pl.UTF-8):	Statyczne biblioteki libuta
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libuta is C++ library which provides a framework for creating
multimedia applications, especially games. It runs on top of SDL and
is available for Win32 and Linux/X11.

This package contains the static libuta.

%description static -l pl.UTF-8
libuta jest biblioteką C++ dającą środowisko do tworzenia aplikacji
multimedialnych, zwłaszcza gier. Opiera się na SDL i jest dostępna pod
Win32 i Linuksa/X11.

Ten pakiet zawiera statyczną bibliotekę libuta.

%prep
%setup -q
%patch -P0

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uta-config
%{_includedir}/uta
%{_libdir}/*.la
%{_libdir}/*.so
%{_aclocaldir}/uta.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
