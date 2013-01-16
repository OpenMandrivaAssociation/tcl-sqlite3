%define realname sqlite
%define realver 3070700
%define rpmver %(echo %{realver}|sed -e "s/00//g" -e "s/0/./g")

Summary:	Tcl binding for sqlite3
Name:		tcl-sqlite3
Version:	%rpmver
Release:	4
License:	Public Domain
Group:		Databases
URL:		http://www.sqlite.org/
Source0:	http://www.sqlite.org/%{realname}-autoconf-%{realver}.tar.gz
Patch0:		sqlite-tea-3070400-link.patch
BuildRequires:	pkgconfig(sqlite3) >= %{rpmver}
BuildRequires:	tcl-devel
BuildRequires:	tcl
Provides:	sqltie3-tcl = %version

%description
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process. The
distribution comes with a standalone command-line access program
(sqlite) that can be used to administer an SQLite database and
which serves as an example of how to use the SQLite library.

This package contains tcl binding for %{name}.

%prep
%setup -q -n %{realname}-autoconf-%{realver}/tea
%patch0 -p0

%build
%configure2_5x --with-system-sqlite --enable-64bit
%make

%install
mkdir -p %{buildroot}%{tcl_sitearch}/sqlite3
install -m755 *.so %{buildroot}%{tcl_sitearch}/sqlite3/
install -m644 pkgIndex.tcl %{buildroot}%{tcl_sitearch}/sqlite3/

%files
%{tcl_sitearch}/sqlite3


%changelog
* Sat Jun 25 2011 Funda Wang <fwang@mandriva.org> 3.7.7-1mdv2011.0
+ Revision: 687072
- new version 3.7.7

* Fri May 20 2011 Funda Wang <fwang@mandriva.org> 3.7.6.3-1
+ Revision: 676385
- 3.7.6.3

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 3.7.6.2-1
+ Revision: 655054
- new version 3.7.6.2
- new version 3.7.6.1

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 3.7.5-2
+ Revision: 640008
- rebuild

* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 3.7.5-1
+ Revision: 634592
- new version 3.7.5

* Wed Jan 26 2011 Funda Wang <fwang@mandriva.org> 3.7.4-1
+ Revision: 632886
- New version 3.7.4
- Created package structure for tcl-sqlite3.

