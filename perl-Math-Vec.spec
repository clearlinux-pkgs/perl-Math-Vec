#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Vec
Version  : 1.01
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/E/EW/EWILHELM/Math-Vec-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EW/EWILHELM/Math-Vec-1.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-vec-perl/libmath-vec-perl_1.01-3.debian.tar.xz
Summary  : Object-Oriented Vector Math Methods in Perl
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Math-Vec-license = %{version}-%{release}
Requires: perl-Math-Vec-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Math-Vec
INSTALLATION
To install this module, run the following commands:
perl Build.PL
./Build
./Build test
./Build install

%package dev
Summary: dev components for the perl-Math-Vec package.
Group: Development
Provides: perl-Math-Vec-devel = %{version}-%{release}
Requires: perl-Math-Vec = %{version}-%{release}

%description dev
dev components for the perl-Math-Vec package.


%package license
Summary: license components for the perl-Math-Vec package.
Group: Default

%description license
license components for the perl-Math-Vec package.


%package perl
Summary: perl components for the perl-Math-Vec package.
Group: Default
Requires: perl-Math-Vec = %{version}-%{release}

%description perl
perl components for the perl-Math-Vec package.


%prep
%setup -q -n Math-Vec-1.01
cd %{_builddir}
tar xf %{_sourcedir}/libmath-vec-perl_1.01-3.debian.tar.xz
cd %{_builddir}/Math-Vec-1.01
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Math-Vec-1.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Vec
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Math-Vec/d768c3dd22dd2af6fe378388e99ea0b6ffb6fb7e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Vec.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Vec/d768c3dd22dd2af6fe378388e99ea0b6ffb6fb7e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
