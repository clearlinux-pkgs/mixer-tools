#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mixer-tools
Version  : 4.5.0
Release  : 80
URL      : https://github.com/clearlinux/mixer-tools/releases/download/v4.5.0/mixer-tools-4.5.0.tar.gz
Source0  : https://github.com/clearlinux/mixer-tools/releases/download/v4.5.0/mixer-tools-4.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : AGPL-3.0 Apache-2.0 BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 GPL-3.0 LGPL-3.0 MIT WTFPL
Requires: mixer-tools-bin
Requires: mixer-tools-data
Requires: mixer-tools-doc
BuildRequires : go

%description
This package uses "dep" tool for vendoring packages, i.e. downloading
the required files to use the package and storing it in the vendor/
subdirectory.

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


%package doc
Summary: doc components for the mixer-tools package.
Group: Documentation

%description doc
doc components for the mixer-tools package.


%prep
%setup -q -n mixer-tools-4.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526343451
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1526343451
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mixer
/usr/bin/mixin

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/mixer
/usr/share/zsh/site-functions/_mixer

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
