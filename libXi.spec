#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXi
Version  : 1.7.6
Release  : 7
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXi-1.7.6.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXi-1.7.6.tar.gz
Summary  : X Input Extension Library
Group    : Development/Tools
License  : MIT-Opengroup
Requires: libXi-lib
Requires: libXi-doc
BuildRequires : asciidoc
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(inputproto)
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


%prep
%setup -q -n libXi-1.7.6

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/XInput.h
/usr/include/X11/extensions/XInput2.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libXi/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
