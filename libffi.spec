#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libffi
Version  : 3.3
Release  : 37
URL      : https://github.com/libffi/libffi/archive/v3.3/libffi-3.3.tar.gz
Source0  : https://github.com/libffi/libffi/archive/v3.3/libffi-3.3.tar.gz
Summary  : Library supporting Foreign Function Interfaces
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: libffi-info = %{version}-%{release}
Requires: libffi-lib = %{version}-%{release}
Requires: libffi-license = %{version}-%{release}
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : tcl
BuildRequires : texinfo
Patch1: 0001-Update-ax_cc_maxopt-m4-macro.patch

%description
Status
======
[![Build Status](https://travis-ci.org/libffi/libffi.svg?branch=master)](https://travis-ci.org/libffi/libffi)
[![Build status](https://ci.appveyor.com/api/projects/status/8lko9vagbx4w2kxq?svg=true)](https://ci.appveyor.com/project/atgreen/libffi)

%package dev
Summary: dev components for the libffi package.
Group: Development
Requires: libffi-lib = %{version}-%{release}
Provides: libffi-devel = %{version}-%{release}
Requires: libffi = %{version}-%{release}

%description dev
dev components for the libffi package.


%package dev32
Summary: dev32 components for the libffi package.
Group: Default
Requires: libffi-lib32 = %{version}-%{release}
Requires: libffi-dev = %{version}-%{release}

%description dev32
dev32 components for the libffi package.


%package info
Summary: info components for the libffi package.
Group: Default

%description info
info components for the libffi package.


%package lib
Summary: lib components for the libffi package.
Group: Libraries
Requires: libffi-license = %{version}-%{release}

%description lib
lib components for the libffi package.


%package lib32
Summary: lib32 components for the libffi package.
Group: Default
Requires: libffi-license = %{version}-%{release}

%description lib32
lib32 components for the libffi package.


%package license
Summary: license components for the libffi package.
Group: Default

%description license
license components for the libffi package.


%prep
%setup -q -n libffi-3.3
cd %{_builddir}/libffi-3.3
%patch1 -p1
pushd ..
cp -a libffi-3.3 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616687223
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1616687223
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libffi
cp %{_builddir}/libffi-3.3/LICENSE %{buildroot}/usr/share/package-licenses/libffi/6ead3a7aa9b1daab14e473e5b0a18383eeb9faee
cp %{_builddir}/libffi-3.3/LICENSE-BUILDTOOLS %{buildroot}/usr/share/package-licenses/libffi/edba73156489a814c9ec38f23fa6aea64efebcbf
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ffi.h
/usr/include/ffitarget.h
/usr/lib64/libffi.so
/usr/lib64/pkgconfig/libffi.pc
/usr/share/man/man3/ffi.3
/usr/share/man/man3/ffi_call.3
/usr/share/man/man3/ffi_prep_cif.3
/usr/share/man/man3/ffi_prep_cif_var.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libffi.so
/usr/lib32/pkgconfig/32libffi.pc
/usr/lib32/pkgconfig/libffi.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libffi.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libffi.so.7
/usr/lib64/libffi.so.7.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libffi.so.7
/usr/lib32/libffi.so.7.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libffi/6ead3a7aa9b1daab14e473e5b0a18383eeb9faee
/usr/share/package-licenses/libffi/edba73156489a814c9ec38f23fa6aea64efebcbf
