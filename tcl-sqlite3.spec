%define realname sqlite
%define realver 3070603
%define rpmver %(echo %{realver}|sed -e "s/00//g" -e "s/0/./g")

Summary:	Tcl binding for sqlite3
Name:		tcl-sqlite3
Version:	%rpmver
Release:	%mkrel 1
License:	Public Domain
Group:		Databases
URL:		http://www.sqlite.org/
Source0:	http://www.sqlite.org/%{realname}-autoconf-%{realver}.tar.gz
Patch0:		sqlite-tea-3070400-link.patch
BuildRequires:	sqlite3-devel >= %{rpmver}
BuildRequires:	tcl-devel
BuildRequires:	tcl
Provides:	sqltie3-tcl = %version
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{tcl_sitearch}/sqlite3
install -m755 *.so %{buildroot}%{tcl_sitearch}/sqlite3/
install -m644 pkgIndex.tcl %{buildroot}%{tcl_sitearch}/sqlite3/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{tcl_sitearch}/sqlite3
