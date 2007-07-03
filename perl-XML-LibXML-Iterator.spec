%define module	XML-LibXML-Iterator
%define name	perl-%{module}
%define version 1.02
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	XML::LibXML's Tree Iteration Class
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  perl-devel 
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::NodeFilter)

%description
XML::LibXML::Iterator is an iterator class for XML::LibXML parsed documents.
This class allows to iterate the document tree as it were a linear data
structure.

%prep
%setup -q -n %{module}-%{version}

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

