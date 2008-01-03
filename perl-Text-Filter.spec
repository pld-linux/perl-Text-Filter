#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Filter
Summary:	Text::Filter perl module
Summary(pl.UTF-8):	Moduł perla Text::Filter
Name:		perl-Text-Filter
Version:	1.9
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	07a37d177d45411a02b68025a542d1a8
URL:		http://search.cpan.org/dist/Text-Filter/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Filter - base class for objects that can read and write text
lines.

%description -l pl.UTF-8
Text::Filter - podstawowa klasa obiektów czytających i zapisujących do
pliku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Text/Filter.pm
%{perl_vendorlib}/Text/Filter
%{_mandir}/man3/*
