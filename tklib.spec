Summary:	Tk Standard Library
Name:		tklib
Version:	0.4.1
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcllib/%{name}-%{version}.tar.gz
# Source0-md5:	4b6919112bc2b9bd816120a8210170b5
URL:		http://tcllib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl
BuildRequires:	tcllib
Requires:	tcllib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		majorver	0.4

%description
Tklib, the Tk Standard Library is a collection of Tcl packages that
provide Tk utility functions and widgets useful to a large collection
of Tcl/Tk programmers.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/lib,%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libdir}/%{name}%{majorver} $RPM_BUILD_ROOT%{_prefix}/lib/%{name}%{majorver}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog DESCRIPTION.txt README README-0.4.txt license.terms examples
%{_prefix}/lib/%{name}%{majorver}
%{_mandir}/man?/*
