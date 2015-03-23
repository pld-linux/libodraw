Summary:	Library to access optical disc (split) RAW formats
Summary(pl.UTF-8):	Biblioteka służąca do dostępu do surowych (podzielonych) formatów dysków optycznych
Name:		libodraw
Version:	20150105
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libodraw/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	193b53914a854694c67972df61ba4a55
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-bison.patch
Patch2:		%{name}-libhmac.patch
Patch3:		%{name}-libcsystem.patch
URL:		https://github.com/libyal/libodraw/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libbfio-devel >= 20120426
BuildRequires:	libcdata-devel >= 20150102
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcfile-devel >= 20140503
BuildRequires:	libclocale-devel >= 20130406
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcpath-devel >= 20120701
BuildRequires:	libcsplit-devel >= 20120701
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcsystem-devel >= 20141018
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libhmac-devel >= 20130714
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libbfio >= 20120426
Requires:	libcdata >= 20150102
Requires:	libcerror >= 20120425
Requires:	libcfile >= 20140503
Requires:	libclocale >= 20130406
Requires:	libcnotify >= 20120425
Requires:	libcpath >= 20120701
Requires:	libcsplit >= 20120701
Requires:	libcstring >= 20120425
Requires:	libcsystem >= 20141018
Requires:	libcthreads >= 20130509
Requires:	libhmac >= 20130714
Requires:	libuna >= 20120425
Requires:	openssl >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libodraw is a library to access optical disc (split) RAW formats.

%description -l pl.UTF-8
libodraw to biblioteka służąca do dostępu do surowych (podzielonych)
formatów dysków optycznych.

%package devel
Summary:	Header files for libodraw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libodraw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbfio-devel >= 20120426
Requires:	libcdata-devel >= 20150102
Requires:	libcerror-devel >= 20120425
Requires:	libcfile-devel >= 20140503
Requires:	libclocale-devel >= 20130406
Requires:	libcnotify-devel >= 20120425
Requires:	libcpath-devel >= 20120701
Requires:	libcsplit-devel >= 20120701
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509
Requires:	libuna-devel >= 20120425

%description devel
Header files for libodraw library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libodraw.

%package static
Summary:	Static libodraw library
Summary(pl.UTF-8):	Statyczna biblioteka libodraw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libodraw library.

%description static -l pl.UTF-8
Statyczna biblioteka libodraw.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libodraw.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/odrawinfo
%attr(755,root,root) %{_bindir}/odrawverify
%attr(755,root,root) %{_libdir}/libodraw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libodraw.so.1
%{_mandir}/man1/odrawinfo.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libodraw.so
%{_includedir}/libodraw
%{_includedir}/libodraw.h
%{_pkgconfigdir}/libodraw.pc
%{_mandir}/man3/libodraw.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libodraw.a
