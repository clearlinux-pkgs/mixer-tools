#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mixer-tools
Version  : 6.2.4
Release  : 186
URL      : https://github.com/clearlinux/mixer-tools/releases/download/v6.2.4/mixer-tools-6.2.4.tar.gz
Source0  : https://github.com/clearlinux/mixer-tools/releases/download/v6.2.4/mixer-tools-6.2.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT
Requires: mixer-tools-bin = %{version}-%{release}
Requires: mixer-tools-data = %{version}-%{release}
Requires: mixer-tools-license = %{version}-%{release}
Requires: mixer-tools-man = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-builder-Add-a-bundle-s-packages-as-the-content-to-th.patch

%description
[![Go Report Card](https://goreportcard.com/badge/github.com/clearlinux/mixer-tools)](https://goreportcard.com/report/github.com/clearlinux/mixer-tools)
[![mixer-tools CI](https://github.com/clearlinux/mixer-tools/workflows/mixer-tools%20CI/badge.svg)](https://github.com/clearlinux/mixer-tools/actions?query=workflow%3A%22mixer-tools+CI%22)

%package bin
Summary: bin components for the mixer-tools package.
Group: Binaries
Requires: mixer-tools-data = %{version}-%{release}
Requires: mixer-tools-license = %{version}-%{release}

%description bin
bin components for the mixer-tools package.


%package data
Summary: data components for the mixer-tools package.
Group: Data

%description data
data components for the mixer-tools package.


%package license
Summary: license components for the mixer-tools package.
Group: Default

%description license
license components for the mixer-tools package.


%package man
Summary: man components for the mixer-tools package.
Group: Default

%description man
man components for the mixer-tools package.


%prep
%setup -q -n mixer-tools-6.2.4
cd %{_builddir}/mixer-tools-6.2.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634321782
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1634321782
rm -rf %{buildroot}
## install_prepend content
export GOFLAGS="-buildmode=pie -v"
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/mixer-tools
cp %{_builddir}/mixer-tools-6.2.4/COPYING %{buildroot}/usr/share/package-licenses/mixer-tools/598f87f072f66e2269dd6919292b2934dbb20492
cp %{_builddir}/mixer-tools-6.2.4/vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/mixer-tools/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
cp %{_builddir}/mixer-tools-6.2.4/vendor/github.com/go-ini/ini/LICENSE %{buildroot}/usr/share/package-licenses/mixer-tools/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a
cp %{_builddir}/mixer-tools-6.2.4/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/mixer-tools/9174f93c54ad0022bbb9b445480cfb6b4217226a
cp %{_builddir}/mixer-tools-6.2.4/vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/mixer-tools/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/mixer-tools-6.2.4/vendor/github.com/olekukonko/tablewriter/LICENSE.md %{buildroot}/usr/share/package-licenses/mixer-tools/7c15369a8295c6d2cd26b41618f5ba81e7e06eca
cp %{_builddir}/mixer-tools-6.2.4/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/mixer-tools/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/mixer-tools-6.2.4/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/mixer-tools/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
cp %{_builddir}/mixer-tools-6.2.4/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/mixer-tools/b3c86ae465b21f7323059db335158b48187731c7
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mixer
/usr/bin/swupd-extract
/usr/bin/swupd-inspector

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/mixer
/usr/share/zsh/site-functions/_mixer

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mixer-tools/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/mixer-tools/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/mixer-tools/7c15369a8295c6d2cd26b41618f5ba81e7e06eca
/usr/share/package-licenses/mixer-tools/9174f93c54ad0022bbb9b445480cfb6b4217226a
/usr/share/package-licenses/mixer-tools/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/mixer-tools/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/mixer-tools/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/mixer-tools/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a
/usr/share/package-licenses/mixer-tools/f9cab757896ef6b3570e62b2df7fb63ab1a34b80

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mixer.1
/usr/share/man/man1/mixer.add-rpms.1
/usr/share/man/man1/mixer.build.1
/usr/share/man/man1/mixer.bundle.1
/usr/share/man/man1/mixer.config.1
/usr/share/man/man1/mixer.init.1
/usr/share/man/man1/mixer.repo.1
/usr/share/man/man1/mixer.versions.1
