#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mixer-tools
Version  : 5.0.0
Release  : 98
URL      : https://github.com/clearlinux/mixer-tools/releases/download/v5.0.0/mixer-tools-5.0.0.tar.gz
Source0  : https://github.com/clearlinux/mixer-tools/releases/download/v5.0.0/mixer-tools-5.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : AGPL-3.0 Apache-2.0 BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 GPL-3.0 LGPL-3.0 MIT WTFPL
Requires: mixer-tools-bin
Requires: mixer-tools-data
Requires: mixer-tools-license
Requires: mixer-tools-man
BuildRequires : buildreq-golang

%description
This package uses "dep" tool for vendoring packages, i.e. downloading
the required files to use the package and storing it in the vendor/
subdirectory.

%package bin
Summary: bin components for the mixer-tools package.
Group: Binaries
Requires: mixer-tools-data
Requires: mixer-tools-license
Requires: mixer-tools-man

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
%setup -q -n mixer-tools-5.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532382814
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1532382814
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/mixer-tools
cp COPYING %{buildroot}/usr/share/doc/mixer-tools/COPYING
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-decoder/COPYING %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-encoder/COPYING %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/tomlv/COPYING %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
cp vendor/github.com/go-ini/ini/LICENSE %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_go-ini_ini_LICENSE
cp vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_inconshreveable_mousetrap_LICENSE
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_LICENSE.txt
cp vendor/github.com/spf13/cobra/cobra/cmd/license_agpl.go %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_agpl.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_apache_2.go %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_apache_2.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_bsd_clause_2.go %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_bsd_clause_2.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_bsd_clause_3.go %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_bsd_clause_3.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_gpl_2.go %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_gpl_2.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_gpl_3.go %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_gpl_3.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_lgpl.go %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_lgpl.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_mit.go %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_mit.go
cp vendor/github.com/spf13/cobra/cobra/cmd/testdata/LICENSE.golden %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_testdata_LICENSE.golden
cp vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/doc/mixer-tools/vendor_github.com_spf13_pflag_LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mixer
/usr/bin/mixin
/usr/bin/swupd-extract
/usr/bin/swupd-inspector

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/mixer
/usr/share/zsh/site-functions/_mixer

%files license
%defattr(-,root,root,-)
/usr/share/doc/mixer-tools/COPYING
/usr/share/doc/mixer-tools/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/doc/mixer-tools/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
/usr/share/doc/mixer-tools/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
/usr/share/doc/mixer-tools/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
/usr/share/doc/mixer-tools/vendor_github.com_go-ini_ini_LICENSE
/usr/share/doc/mixer-tools/vendor_github.com_inconshreveable_mousetrap_LICENSE
/usr/share/doc/mixer-tools/vendor_github.com_pkg_errors_LICENSE
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_LICENSE.txt
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_agpl.go
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_apache_2.go
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_bsd_clause_2.go
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_bsd_clause_3.go
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_gpl_2.go
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_gpl_3.go
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_lgpl.go
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_license_mit.go
/usr/share/doc/mixer-tools/vendor_github.com_spf13_cobra_cobra_cmd_testdata_LICENSE.golden
/usr/share/doc/mixer-tools/vendor_github.com_spf13_pflag_LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/mixer.1
/usr/share/man/man1/mixer.add-rpms.1
/usr/share/man/man1/mixer.build.1
/usr/share/man/man1/mixer.bundle.1
/usr/share/man/man1/mixer.config.1
/usr/share/man/man1/mixer.init.1
/usr/share/man/man1/mixer.repo.1
/usr/share/man/man1/mixer.versions.1
/usr/share/man/man1/mixin.1
