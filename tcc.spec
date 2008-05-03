Summary:	Tiny C Compiler
Summary(pl.UTF-8):	Mały kompilator C
Name:		tcc
Version:	0.9.24
Release:	1
License:	LGPL
Group:		Development/Languages
Source0:	http://download.savannah.nongnu.org/releases/tinycc/%{name}-%{version}.tar.bz2
# Source0-md5:	24d8442d1f2c0a4c2cafb6859c333b05
Patch0:		%{name}-DESTDIR.patch
ExclusiveArch:	%{ix86}
URL:		http://fabrice.bellard.free.fr/tcc/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tiny C Compiler - C Scripting Everywhere - The Smallest ANSI C
compiler.

%description -l pl.UTF-8
Mały kompilator C - Wszędzie skrypty w C - Najmniejszy kompilator ANSI
C.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc Changelog README TODO tcc-doc.html
%attr(755,root,root) %{_bindir}/*
%{_libdir}/lib*.a
%{_libdir}/tcc
%{_includedir}/*.h
%{_mandir}/man?/*
