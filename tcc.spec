Summary:	Tiny C Compiler
Summary(pl):	Ma³y kompilator C
Name:		tcc
Version:	0.9.20
Release:	1
License:	LGPL
Group:		Development/Languages
URL:		http://fabrice.bellard.free.fr/tcc/
Source0:	http://fabrice.bellard.free.fr/tcc/%{name}-%{version}.tar.gz
# Source0-md5:	c883b88e874a9bb9163eb14dc43b178c
Patch0:		%{name}-DESTDIR.patch
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
%doc COPYING Changelog README TODO VERSION
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_mandir}/man?/*
