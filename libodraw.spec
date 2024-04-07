# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver	20201125
%define		libcdata_ver	20230108
%define		libcerror_ver	20120425
%define		libcfile_ver	20160409
%define		libclocale_ver	20130406
%define		libcnotify_ver	20120425
%define		libcpath_ver	20180716
%define		libcsplit_ver	20120701
%define		libcthreads_ver	20160404
%define		libhmac_ver	20200104
%define		libuna_ver	20230702
Summary:	Library to access optical disc (split) RAW formats
Summary(pl.UTF-8):	Biblioteka służąca do dostępu do surowych (podzielonych) formatów dysków optycznych
Name:		libodraw
Version:	20240306
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libodraw/releases
Source0:	https://github.com/libyal/libodraw/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	ac6b32c1e1722a609caf91be69173489
URL:		https://github.com/libyal/libodraw/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libhmac-devel >= %{libhmac_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 1.0
BuildRequires:	pkgconfig
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcfile >= %{libcfile_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcpath >= %{libcpath_ver}
Requires:	libcsplit >= %{libcsplit_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libhmac >= %{libhmac_ver}
Requires:	libuna >= %{libuna_ver}
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
Requires:	libbfio-devel >= %{libbfio_ver}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcfile-devel >= %{libcfile_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcpath-devel >= %{libcpath_ver}
Requires:	libcsplit-devel >= %{libcsplit_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libuna-devel >= %{libuna_ver}

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

%build
%{__gettextize}
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
