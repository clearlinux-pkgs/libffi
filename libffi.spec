#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libffi
Version  : 3.2.1
Release  : 18
URL      : ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz
Source0  : ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz
Summary  : Library supporting Foreign Function Interfaces
Group    : Development/Tools
License  : MIT
Requires: libffi-lib
Requires: libffi-doc
BuildRequires : autogen
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : tcl

%description
Status
======
libffi-3.2.1 was released on November 12, 2014.  Check the libffi web
page for updates: <URL:http://sourceware.org/libffi/>.

%package dev
Summary: dev components for the libffi package.
Group: Development
Requires: libffi-lib

%description dev
dev components for the libffi package.


%package doc
Summary: doc components for the libffi package.
Group: Documentation

%description doc
doc components for the libffi package.


%package lib
Summary: lib components for the libffi package.
Group: Libraries

%description lib
lib components for the libffi package.


%prep
%setup -q -n libffi-3.2.1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/*.so
/usr/lib64/libffi-3.2.1/include/ffi.h
/usr/lib64/libffi-3.2.1/include/ffitarget.h
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*