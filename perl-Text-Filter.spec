%include	/usr/lib/rpm/macros.perl
Summary:	Text-Filter perl module
Summary(pl):	Modu³ perla Text-Filter
Name:		perl-Text-Filter
Version:	1.7
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Filter-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Filter - base class for objects that can read and write text lines.

%description -l pl
Text-Filter - podstawowa klasa obiektów czytaj±cych i zapisuj±cych do pliku.

%prep
%setup -q -n Text-Filter-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/Filter
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README AVAILABILITY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,AVAILABILITY}.gz

%{perl_sitelib}/Text/Filter.pm
%{perl_sitearch}/auto/Text/Filter

%{_mandir}/man3/*
