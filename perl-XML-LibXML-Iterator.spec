%define upstream_name	 XML-LibXML-Iterator
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	XML::LibXML's Tree Iteration Class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::NodeFilter)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
XML::LibXML::Iterator is an iterator class for XML::LibXML parsed documents.
This class allows to iterate the document tree as it were a linear data
structure.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML/*
%{_mandir}/*/*
