#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : libXi
Version  : 1.7.9
Release  : 16
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXi-1.7.9.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXi-1.7.9.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/lib/libXi-1.7.9.tar.gz.sig
Summary  : X Input Extension Library
Group    : Development/Tools
License  : MIT-Opengroup
Requires: libXi-lib
Requires: libXi-doc
BuildRequires : asciidoc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32inputproto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : xmlto

%description
libXi - library for the X Input Extension
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the libXi package.
Group: Development
Requires: libXi-lib
Provides: libXi-devel

%description dev
dev components for the libXi package.


%package dev32
Summary: dev32 components for the libXi package.
Group: Default
Requires: libXi-lib32
Requires: libXi-dev

%description dev32
dev32 components for the libXi package.


%package doc
Summary: doc components for the libXi package.
Group: Documentation

%description doc
doc components for the libXi package.


%package lib
Summary: lib components for the libXi package.
Group: Libraries

%description lib
lib components for the libXi package.


%package lib32
Summary: lib32 components for the libXi package.
Group: Default

%description lib32
lib32 components for the libXi package.


%prep
%setup -q -n libXi-1.7.9
pushd ..
cp -a libXi-1.7.9 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491880108
export CFLAGS="$CFLAGS -Os -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491880108
rm -rf %{buildroot}
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
/usr/include/X11/extensions/XInput.h
/usr/include/X11/extensions/XInput2.h
/usr/lib64/libXi.so
/usr/lib64/pkgconfig/xi.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXi.so
/usr/lib32/pkgconfig/32xi.pc
/usr/lib32/pkgconfig/xi.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libXi/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXi.so.6
/usr/lib64/libXi.so.6.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXi.so.6
/usr/lib32/libXi.so.6.1.0
