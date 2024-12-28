%global moh_dir %{_datadir}/asterisk/moh
%global moh_version 2.03

Name:           asterisk-moh-opsound
Version:        2.0.3
Release:        1%{?dist}
Summary:        MOH opsound for Asterisk

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://www.asterisk.org/

Source0:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-alaw-%{moh_version}.tar.gz
Source1:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-g722-%{moh_version}.tar.gz
Source2:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-g729-%{moh_version}.tar.gz
Source3:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-gsm-%{moh_version}.tar.gz
Source4:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-siren14-%{moh_version}.tar.gz
Source5:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-siren7-%{moh_version}.tar.gz
Source6:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-sln16-%{moh_version}.tar.gz
Source7:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-ulaw-%{moh_version}.tar.gz
Source8:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-wav-%{moh_version}.tar.gz

BuildArch:      noarch

%description
MOH opsound files for Asterisk.

%package alaw
Summary: MOH opsound ALAW files for Asterisk
Requires: asterisk >= 1.4.0
Provides: asterisk-moh-opsound = %{version}-%{release}

%description alaw
MOH opsound ALAW files for Asterisk.

%package g722
Summary: MOH opsound G.722 files for Asterisk
Requires: asterisk >= 1.4.0
Provides: asterisk-moh-opsound = %{version}-%{release}

%description g722
MOH opsound G.722 files for Asterisk.

%package g729
Summary: MOH opsound G.729 files for Asterisk
Requires: asterisk >= 1.4.0
Provides: asterisk-moh-opsound = %{version}-%{release}

%description g729
MOH opsound G.729 files for Asterisk.

%package gsm
Summary: MOH opsound GSM files for Asterisk
Requires: asterisk >= 1.4.0
Provides: asterisk-moh-opsound = %{version}-%{release}

%description gsm
MOH opsound GSM files for Asterisk.

%package siren7
Summary: MOH opsound Siren7 files for Asterisk
Requires: asterisk >= 1.4.0
Provides: asterisk-moh-opsound = %{version}-%{release}

%description siren7
MOH opsound Siren7 files for Asterisk.

%package siren14
Summary: MOH opsound Siren14 files for Asterisk
Requires: asterisk >= 1.4.0
Provides: asterisk-moh-opsound = %{version}-%{release}

%description siren14
MOH opsound Siren14 files for Asterisk.

%package sln16
Summary: MOH opsound SLN16 files for Asterisk
Requires: asterisk >= 1.4.0
Provides: asterisk-moh-opsound = %{version}-%{release}

%description sln16
MOH opsound SLN16 files for Asterisk.

%package ulaw
Summary: MOH opsound ULAW files for Asterisk
Requires: asterisk >= 1.4.0
Provides: asterisk-moh-opsound = %{version}-%{release}

%description ulaw
MOH opsound ULAW files for Asterisk.

%package wav
Summary: MOH opsound WAV files for Asterisk
Requires: asterisk >= 1.4.0
Provides: asterisk-moh-opsound = %{version}-%{release}

%description wav
MOH opsound WAV files for Asterisk.

%prep

%setup -c -T 

%build

for file in %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{moh_dir}/!' > `basename $file .tar.gz`.list
  tar --extract --directory . --file $file
done

%install
rm -rf %{buildroot}

for file in `cat *.list | sed -e 's!^%{moh_dir}/!!'`
do
  mkdir -p %{buildroot}%{moh_dir}/`dirname $file`
  cp -p $file %{buildroot}%{moh_dir}/$file
done

%files alaw -f asterisk-moh-opsound-alaw-%{moh_version}.list
%doc CHANGES-asterisk-moh-opsound-alaw
%doc CREDITS-asterisk-moh-opsound-alaw
%license LICENSE-asterisk-moh-opsound-alaw
%doc asterisk-moh-opsound-alaw-%{moh_version}.list

%files g722 -f asterisk-moh-opsound-g722-%{moh_version}.list
%doc CHANGES-asterisk-moh-opsound-g722
%doc CREDITS-asterisk-moh-opsound-g722
%license LICENSE-asterisk-moh-opsound-g722
%doc asterisk-moh-opsound-g722-%{moh_version}.list

%files g729 -f asterisk-moh-opsound-g729-%{moh_version}.list
%doc CHANGES-asterisk-moh-opsound-g729
%doc CREDITS-asterisk-moh-opsound-g729
%license LICENSE-asterisk-moh-opsound-g729
%doc asterisk-moh-opsound-g729-%{moh_version}.list

%files gsm -f asterisk-moh-opsound-gsm-%{moh_version}.list
%doc CHANGES-asterisk-moh-opsound-gsm
%doc CREDITS-asterisk-moh-opsound-gsm
%license LICENSE-asterisk-moh-opsound-gsm
%doc asterisk-moh-opsound-gsm-%{moh_version}.list

%files siren7 -f asterisk-moh-opsound-siren7-%{moh_version}.list
%doc CHANGES-asterisk-moh-opsound-siren7
%doc CREDITS-asterisk-moh-opsound-siren7
%license LICENSE-asterisk-moh-opsound-siren7
%doc asterisk-moh-opsound-siren7-%{moh_version}.list

%files siren14 -f asterisk-moh-opsound-siren14-%{moh_version}.list
%doc CHANGES-asterisk-moh-opsound-siren14
%doc CREDITS-asterisk-moh-opsound-siren14
%license LICENSE-asterisk-moh-opsound-siren14
%doc asterisk-moh-opsound-siren14-%{moh_version}.list

%files sln16 -f asterisk-moh-opsound-sln16-%{moh_version}.list
%doc CHANGES-asterisk-moh-opsound-sln16
%doc CREDITS-asterisk-moh-opsound-sln16
%license LICENSE-asterisk-moh-opsound-sln16
%doc asterisk-moh-opsound-sln16-%{moh_version}.list

%files ulaw -f asterisk-moh-opsound-ulaw-%{moh_version}.list
%doc CHANGES-asterisk-moh-opsound-ulaw
%doc CREDITS-asterisk-moh-opsound-ulaw
%license LICENSE-asterisk-moh-opsound-ulaw
%doc asterisk-moh-opsound-ulaw-%{moh_version}.list

%files wav -f asterisk-moh-opsound-wav-%{moh_version}.list
%doc CHANGES-asterisk-moh-opsound-wav
%doc CREDITS-asterisk-moh-opsound-wav
%license LICENSE-asterisk-moh-opsound-wav
%doc asterisk-moh-opsound-wav-%{moh_version}.list

%changelog
* Fri Dec 27 2024 Luis Leal <Luis Leal> - 2.0.3-1
- Initial MOH opsound 

