%define upstream_name    Email-Verify-SMTP
%define upstream_version 0.003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Specify dependencies on external non-Perl things
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IO::Socket::Telnet)
BuildRequires:	perl(Net::Nslookup)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
'Email::Verify::Simple' is what I came with when I needed to verify several
email addresses without actually sending them email.

To put that another way:

    *This module verifies email addresses without actually sending email to
    them.*

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.3.0-2mdv2011.0
+ Revision: 654316
- rebuild for updated spec-helper

* Sun Oct 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 582708
- import perl-Email-Verify-SMTP

