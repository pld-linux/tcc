Summary:	Tiny C Compiler
Summary(pl.UTF-8):	Mały kompilator C
Name:		tcc
Version:	0.9.26
Release:	1
License:	GPL v2+ with linking exception
Group:		Development/Languages
Source0:	http://download.savannah.nongnu.org/releases/tinycc/%{name}-%{version}.tar.bz2
# Source0-md5:	5fb28e4abc830c46a7f54c1f637fb25d
Patch0:		%{name}-info.patch
URL:		http://bellard.org/tcc/
BuildRequires:	texinfo
ExclusiveArch:	%{ix86} %{x8664} arm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tiny C Compiler - C Scripting Everywhere - The Smallest ANSI C
compiler.

%description -l pl.UTF-8
Mały kompilator C - wszędzie dostępne skrypty w C - najmniejszy
kompilator ANSI C.

%prep
%setup -q
%patch0 -p1

%build
# not autoconf configure
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--cc="%{__cc}" \
	--extra-cflags="%{rpmcflags}" \
	--extra-ldflags="%{rpmldflags}" \

%{__make}
#	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/tcc/tcc-doc.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TODO tcc-doc.html
%attr(755,root,root) %{_bindir}/tcc
%{_libdir}/libtcc.a
%{_libdir}/tcc
%{_includedir}/libtcc.h
%{_infodir}/tcc-doc.info*
%{_mandir}/man1/tcc.1*
