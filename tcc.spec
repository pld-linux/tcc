Summary:	Tiny C Compiler
Summary(pl):	Ma³y kompilator C
Name:		tcc
Version:	0.9.21
Release:	1
License:	LGPL
Group:		Development/Languages
Source0:	http://fabrice.bellard.free.fr/tcc/%{name}-%{version}.tar.gz
# Source0-md5:	364eb218266e5bd4dc97752e6c111d14
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-regparm.patch
ExclusiveArch:	%{ix86}
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
%patch0 -p1
%patch1 -p1

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
