Summary:	Tiny C Compiler
Summary(pl):	Ma³y kompilator C
Name:		tcc
Version:	0.9.20
Release:	3
License:	LGPL
Group:		Development/Languages
Source0:	http://fabrice.bellard.free.fr/tcc/%{name}-%{version}.tar.gz
# Source0-md5:	c883b88e874a9bb9163eb14dc43b178c
Patch0:		%{name}-DESTDIR.patch
ExclusiveArch:	%{x86}
URL:		http://fabrice.bellard.free.fr/tcc/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tiny C Compiler - C Scripting Everywhere - The Smallest ANSI C
compiler.

%description -l pl
Ma³y kompilator C - Wszêdzie skrypty w C - Najmniejszy kompilator ANSI
C.

%prep
%setup -q
%patch0 -p0

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
%doc Changelog README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/lib*.a
%{_libdir}/tcc
%{_includedir}/*.h
%{_mandir}/man?/*
