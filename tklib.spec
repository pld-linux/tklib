Summary:	Tk Standard Library
Summary(pl.UTF-8):	Biblioteka standardowa Tk
Name:		tklib
Version:	0.5
Release:	2
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://downloads.sourceforge.net/tcllib/%{name}-%{version}.tar.gz
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

%package demo
Summary:	Demo for %{name}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{name}
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{name}.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/lib,%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if "%{_lib}" != "lib"
mv $RPM_BUILD_ROOT%{_libdir}/%{name}%{majorver} $RPM_BUILD_ROOT%{_prefix}/lib/%{name}%{majorver}
%endif

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog DESCRIPTION.txt README README-0.4.txt license.terms
%dir %{_prefix}/lib/%{name}%{majorver}
%{_prefix}/lib/%{name}%{majorver}/autoscroll
%{_prefix}/lib/%{name}%{majorver}/canvas
%{_prefix}/lib/%{name}%{majorver}/chatwidget
%{_prefix}/lib/%{name}%{majorver}/crosshair
%{_prefix}/lib/%{name}%{majorver}/ctext
%{_prefix}/lib/%{name}%{majorver}/cursor
%{_prefix}/lib/%{name}%{majorver}/datefield
%{_prefix}/lib/%{name}%{majorver}/diagrams
%{_prefix}/lib/%{name}%{majorver}/getstring
%{_prefix}/lib/%{name}%{majorver}/history
%{_prefix}/lib/%{name}%{majorver}/ico
%{_prefix}/lib/%{name}%{majorver}/ipentry
%{_prefix}/lib/%{name}%{majorver}/khim
%{_prefix}/lib/%{name}%{majorver}/ntext
%{_prefix}/lib/%{name}%{majorver}/pkgIndex.tcl
%{_prefix}/lib/%{name}%{majorver}/plotchart
%{_prefix}/lib/%{name}%{majorver}/style
%{_prefix}/lib/%{name}%{majorver}/swaplist
%{_prefix}/lib/%{name}%{majorver}/tablelist
%{_prefix}/lib/%{name}%{majorver}/tkpiechart
%{_prefix}/lib/%{name}%{majorver}/tooltip
%{_prefix}/lib/%{name}%{majorver}/widget
%{_mandir}/mann/*.n*

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
