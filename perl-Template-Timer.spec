%define realname Template-Timer
%define name perl-%{realname}
%define version 0.04
%define release %mkrel 3

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

