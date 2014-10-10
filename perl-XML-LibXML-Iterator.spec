%define upstream_name	 XML-LibXML-Iterator
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	XML::LibXML's Tree Iteration Class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::NodeFilter)
BuildArch:	noarch

%description
XML::LibXML::Iterator is an iterator class for XML::LibXML parsed documents.
This class allows to iterate the document tree as it were a linear data
structure.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/*
%{_mandir}/*/*

%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 408240
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.04-3mdv2009.0
+ Revision: 242245
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Oct 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2008.0
+ Revision: 98174
- update to new version 1.04
- update to new version 1.04

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2008.0
+ Revision: 63980
- update to new version 1.03

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2008.0
+ Revision: 47741
- update to new version 1.02


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.00-4mdk
- Fix According to perl Policy
	- Source URL
	- BuildRequires

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.00-3mdk
- fix BuildRequires

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 1.00-2mdk
- BuildRequires

* Mon Aug 30 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.00-1mdk
- Initial MDK release, needed by perl-XML-XUpdate-LibXML.

