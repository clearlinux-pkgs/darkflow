#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : darkflow
Version  : master
Release  : 15
URL      : https://github.com/thtrieu/darkflow/archive/master.tar.gz
Source0  : https://github.com/thtrieu/darkflow/archive/master.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: darkflow-bin = %{version}-%{release}
Requires: darkflow-license = %{version}-%{release}
Requires: darkflow-python = %{version}-%{release}
Requires: darkflow-python3 = %{version}-%{release}
BuildRequires : Cython-python3
BuildRequires : buildreq-distutils3
BuildRequires : numpy

%description
## Intro
[![Build Status](https://travis-ci.org/thtrieu/darkflow.svg?branch=master)](https://travis-ci.org/thtrieu/darkflow) [![codecov](https://codecov.io/gh/thtrieu/darkflow/branch/master/graph/badge.svg)](https://codecov.io/gh/thtrieu/darkflow)

%package bin
Summary: bin components for the darkflow package.
Group: Binaries
Requires: darkflow-license = %{version}-%{release}

%description bin
bin components for the darkflow package.


%package license
Summary: license components for the darkflow package.
Group: Default

%description license
license components for the darkflow package.


%package python
Summary: python components for the darkflow package.
Group: Default
Requires: darkflow-python3 = %{version}-%{release}

%description python
python components for the darkflow package.


%package python3
Summary: python3 components for the darkflow package.
Group: Default
Requires: python3-core

%description python3
python3 components for the darkflow package.


%prep
%setup -q -n darkflow-master
cd %{_builddir}/darkflow-master

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582915768
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/darkflow
cp %{_builddir}/darkflow-master/LICENSE %{buildroot}/usr/share/package-licenses/darkflow/12d81f50767d4e09aa7877da077ad9d1b915d75b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flow

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/darkflow/12d81f50767d4e09aa7877da077ad9d1b915d75b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
