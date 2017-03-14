#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mixer-tools
Version  : 3.03
Release  : 39
URL      : https://github.com/clearlinux/mixer-tools/archive/v3.03.tar.gz
Source0  : https://github.com/clearlinux/mixer-tools/archive/v3.03.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mixer-tools-bin
Requires: mixer-tools-data
BuildRequires : go

%description
This project contains tooling for using the software update mixer.

%package bin
Summary: bin components for the mixer-tools package.
Group: Binaries
Requires: mixer-tools-data

%description bin
bin components for the mixer-tools package.


%package data
Summary: data components for the mixer-tools package.
Group: Data

%description data
data components for the mixer-tools package.


%prep
%setup -q -n mixer-tools-3.03

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489516077
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1489516077
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mixer
/usr/bin/mixer-pack-maker.sh
/usr/bin/mixer-superpack-maker.sh

%files data
%defattr(-,root,root,-)
/usr/share/defaults/mixer/yum.conf.in
