%include	/usr/lib/rpm/macros.perl
Summary:	Text-Filter perl module
Summary(pl):	Modu³ perla Text-Filter
Name:		perl-Text-Filter
Version:	1.7
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Filter-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Filter - base class for objects that can read and write text
lines.

%description -l pl
Text-Filter - podstawowa klasa obiektów czytaj±cych i zapisuj±cych do
pliku.

%prep
%setup -q -n Text-Filter-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README AVAILABILITY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/Filter.pm
%{_mandir}/man3/*
