%define realname Template-Timer
%define name perl-%{realname}
%define version 1.00
%define release 3

Summary:	Rudimentary profiling for Template Toolkit
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl-Template-Toolkit
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
Template::Timer provides inline timings of the template processing througout
your code. It's an overridden version of Template::Context that wraps the
process() and include() methods.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Template/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT



%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.00-2mdv2010.0
+ Revision: 440695
- rebuild

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2009.1
+ Revision: 353017
- update to new version 1.00

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.04-5mdv2009.0
+ Revision: 241952
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.04-3mdv2008.0
+ Revision: 23835
- rebuild


* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- Add BuildRequires

* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-1mdk
- Initial MDV RPM

