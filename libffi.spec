#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v21
# autospec commit: 8b93847
#
Name     : libffi
Version  : 3.4.7
Release  : 41
URL      : https://github.com/libffi/libffi/archive/v3.4.7/libffi-3.4.7.tar.gz
Source0  : https://github.com/libffi/libffi/archive/v3.4.7/libffi-3.4.7.tar.gz
Summary  : Library supporting Foreign Function Interfaces
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: libffi-info = %{version}-%{release}
Requires: libffi-lib = %{version}-%{release}
Requires: libffi-license = %{version}-%{release}
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : file
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : tcl
BuildRequires : texinfo
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Status
======
libffi-3.4.7 was released on February 8, 2025.  Check the libffi web
page for updates: <URL:http://sourceware.org/libffi/>.

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
%setup -q -n libffi-3.4.7
cd %{_builddir}/libffi-3.4.7
pushd ..
cp -a libffi-3.4.7 build32
popd
pushd ..
cp -a libffi-3.4.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739229936
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%autogen --disable-static
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
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1739229936
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libffi
cp %{_builddir}/libffi-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libffi/a108ca721195dac8b4bcbd4182e024b1357109d7 || :
cp %{_builddir}/libffi-%{version}/LICENSE-BUILDTOOLS %{buildroot}/usr/share/package-licenses/libffi/edba73156489a814c9ec38f23fa6aea64efebcbf || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/libffi.so.8.1.4
/usr/lib64/libffi.so.8
/usr/lib64/libffi.so.8.1.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libffi.so.8
/usr/lib32/libffi.so.8.1.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libffi/a108ca721195dac8b4bcbd4182e024b1357109d7
/usr/share/package-licenses/libffi/edba73156489a814c9ec38f23fa6aea64efebcbf
