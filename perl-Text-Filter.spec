%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Filter
Summary:	Text-Filter perl module
Summary(pl):	Modu� perla Text-Filter
Name:		perl-Text-Filter
Version:	1.7
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Filter - base class for objects that can read and write text
lines.

%description -l pl
Text-Filter - podstawowa klasa obiekt�w czytaj�cych i zapisuj�cych do
pliku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
