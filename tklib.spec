Summary:	Tk Standard Library
Summary(pl.UTF-8):	Biblioteka standardowa Tk
Name:		tklib
Version:	0.5
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcllib/%{name}-%{version}.tar.gz
# Source0-md5:	c8b84f3eb4dafbd4e5818e29d408faea
URL:		http://tcllib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl
BuildRequires:	tcllib
Requires:	tcllib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		majorver	0.5

%description
Tklib, the Tk Standard Library is a collection of Tcl packages that
provide Tk utility functions and widgets useful to a large collection
of Tcl/Tk programmers.

%description -l pl.UTF-8
Tklib - biblioteka standardowa Tk - to zestaw pakietów Tcl-a
udostępniających funkcje narzędziowe i widgety Tk przydatne znacznej
części programistów Tcl/Tk.

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

%ifarch x86_64
mv $RPM_BUILD_ROOT%{_libdir}/%{name}%{majorver} $RPM_BUILD_ROOT%{_prefix}/lib/%{name}%{majorver}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog DESCRIPTION.txt README README-0.4.txt license.terms examples
%{_prefix}/lib/%{name}%{majorver}
%{_mandir}/man?/*
