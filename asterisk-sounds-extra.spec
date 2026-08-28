%global sounds_dir %{_datadir}/asterisk/sounds
%global en_GB_version 1.5.2
%global en_version 1.5.2
%global fr_version 1.5.2

Name:           asterisk-sounds-extra
Version:        1.5.2
Release:        1%{?dist}
Summary:        Extra sounds for Asterisk

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://www.asterisk.org/

Source0:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-alaw-%{en_version}.tar.gz
Source1:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-g722-%{en_version}.tar.gz
Source2:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-g729-%{en_version}.tar.gz
Source3:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-gsm-%{en_version}.tar.gz
Source4:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-siren7-%{en_version}.tar.gz
Source5:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-siren14-%{en_version}.tar.gz
Source6:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-sln16-%{en_version}.tar.gz
Source7:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-ulaw-%{en_version}.tar.gz
Source8:        https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-wav-%{en_version}.tar.gz

Source10:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-alaw-%{fr_version}.tar.gz
Source11:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-g722-%{fr_version}.tar.gz
Source12:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-g729-%{fr_version}.tar.gz
Source13:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-gsm-%{fr_version}.tar.gz
Source14:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-siren7-%{fr_version}.tar.gz
Source15:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-siren14-%{fr_version}.tar.gz
Source16:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-sln16-%{fr_version}.tar.gz
Source17:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-ulaw-%{fr_version}.tar.gz
Source18:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-wav-%{fr_version}.tar.gz

Source20:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en_GB-alaw-%{en_GB_version}.tar.gz
Source21:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en_GB-g722-%{en_GB_version}.tar.gz
Source22:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en_GB-g729-%{en_GB_version}.tar.gz
Source23:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en_GB-gsm-%{en_GB_version}.tar.gz
Source24:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en_GB-siren7-%{en_GB_version}.tar.gz
Source25:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en_GB-siren14-%{en_GB_version}.tar.gz
Source26:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en_GB-sln16-%{en_GB_version}.tar.gz
Source27:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en_GB-ulaw-%{en_GB_version}.tar.gz
Source28:       https://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en_GB-wav-%{en_GB_version}.tar.gz

BuildArch:      noarch

%description
Extra sound files for Asterisk.

%package en
Summary: Extra English sound files for Asterisk
Requires: asterisk >= 1.4.0

%description en
Extra English sound files for Asterisk.

%package en-alaw
Summary: Extra English ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en-alaw
Extra English ALAW sound files for Asterisk.

%package en-g722
Summary: Extra English G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en-g722
Extra English G.722 sound files for Asterisk.

%package en-g729
Summary: Extra English G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en-g729
Extra English G.729 sound files for Asterisk.

%package en-gsm
Summary: Extra English GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en-gsm
Extra English GSM sound files for Asterisk.

%package en-siren7
Summary: Extra English Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en-siren7
Extra English Siren7 sound files for Asterisk.

%package en-siren14
Summary: Extra English GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en-siren14
Extra English Siren14 sound files for Asterisk.

%package en-sln16
Summary: Extra English SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en-sln16
Extra English SLN16 sound files for Asterisk.

%package en-ulaw
Summary: Extra English ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en-ulaw
Extra English ULAW sound files for Asterisk.

%package en-wav
Summary: Extra English WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en-wav
Extra English WAV sound files for Asterisk.

%package fr
Summary: Extra French sound files for Asterisk
Requires: asterisk >= 1.4.0

%description fr
Extra French sound files for Asterisk.

%package fr-alaw
Summary: Extra French ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-fr = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description fr-alaw
Extra French ALAW sound files for Asterisk.

%package fr-g722
Summary: Extra French G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-fr = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description fr-g722
Extra French G.722 sound files for Asterisk.

%package fr-g729
Summary: Extra French G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-fr = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description fr-g729
Extra French G.729 sound files for Asterisk.

%package fr-gsm
Summary: Extra French GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-fr = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description fr-gsm
Extra French GSM sound files for Asterisk.

%package fr-siren7
Summary: Extra French Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-fr = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description fr-siren7
Extra French Siren7 sound files for Asterisk.

%package fr-siren14
Summary: Extra French Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-fr = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description fr-siren14
Extra French Siren14 sound files for Asterisk.

%package fr-sln16
Summary: Extra French SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-fr = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description fr-sln16
Extra French SLN16 sound files for Asterisk.

%package fr-ulaw
Summary: Extra French ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-fr = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description fr-ulaw
Extra French ULAW sound files for Asterisk.

%package fr-wav
Summary: Extra French WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-fr = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description fr-wav
Extra French WAV sound files for Asterisk.

%package en_GB
Summary: Extra English (United Kingdom) sound files for Asterisk
Requires: asterisk >= 1.4.0

%description en_GB
Extra English (United Kingdom) sound files for Asterisk.

%package en_GB-alaw
Summary: Extra English (United Kingdom) ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en_GB = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en_GB-alaw
Extra English (United Kingdom) ALAW sound files for Asterisk.

%package en_GB-g722
Summary: Extra English (United Kingdom) G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en_GB = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en_GB-g722
Extra English (United Kingdom) G.722 sound files for Asterisk.

%package en_GB-g729
Summary: Extra English (United Kingdom) G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en_GB = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en_GB-g729
Extra English (United Kingdom) G.729 sound files for Asterisk.

%package en_GB-gsm
Summary: Extra English (United Kingdom) GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en_GB = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en_GB-gsm
Extra English (United Kingdom) GSM sound files for Asterisk.

%package en_GB-siren7
Summary: Extra English (United Kingdom) Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en_GB = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en_GB-siren7
Extra English (United Kingdom) Siren7 sound files for Asterisk.

%package en_GB-siren14
Summary: Extra English (United Kingdom) Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en_GB = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en_GB-siren14
Extra English (United Kingdom) Siren14 sound files for Asterisk.

%package en_GB-sln16
Summary: Extra English (United Kingdom) SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en_GB = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en_GB-sln16
Extra English (United Kingdom) SLN16 sound files for Asterisk.

%package en_GB-ulaw
Summary: Extra English (United Kingdom) ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en_GB = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en_GB-ulaw
Extra English (United Kingdom) ULAW sound files for Asterisk.

%package en_GB-wav
Summary: Extra English (United Kingdom) WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-extra-en_GB = %{version}-%{release}
Provides: asterisk-sounds-extra = %{version}-%{release}

%description en_GB-wav
Extra English (United Kingdom) WAV sound files for Asterisk.

%prep

%setup -c -T 

%build

for file in %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/!' > `basename $file .tar.gz`.list
  tar --extract --directory . --file $file
done

mkdir fr

for file in %{S:10} %{S:11} %{S:12} %{S:13} %{S:14} %{S:15} %{S:16} %{S:17} %{S:18}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/fr/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./fr/  --file $file
done

iconv -f iso-8859-1 -t utf-8 < fr/extra-sounds-fr.txt > fr/extra-sounds-fr.txt.tmp
touch --reference fr/extra-sounds-fr.txt fr/extra-sounds-fr.txt.tmp
mv fr/extra-sounds-fr.txt.tmp fr/extra-sounds-fr.txt

mkdir en_GB

for file in %{S:20} %{S:21} %{S:22} %{S:23} %{S:24} %{S:25} %{S:26} %{S:27} %{S:28}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/en_GB/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./en_GB/  --file $file
done

%install
rm -rf %{buildroot}

for file in `cat *.list | sed -e 's!^%{sounds_dir}/!!'`
do
  mkdir -p %{buildroot}%{sounds_dir}/`dirname $file`
  cp -p $file %{buildroot}%{sounds_dir}/$file
done

%files en
%doc extra-sounds-en.txt
%doc CHANGES-asterisk-extra-en-%{en_version}
%doc CREDITS-asterisk-extra-en-%{en_version}
%license LICENSE-asterisk-extra-en-%{en_version}
%dir %{sounds_dir}/ha/
%dir %{sounds_dir}/wx/

%files en-alaw -f asterisk-extra-sounds-en-alaw-%{en_version}.list
%doc asterisk-extra-sounds-en-alaw-%{en_version}.list

%files en-g722 -f asterisk-extra-sounds-en-g722-%{en_version}.list
%doc asterisk-extra-sounds-en-g722-%{en_version}.list

%files en-g729 -f asterisk-extra-sounds-en-g729-%{en_version}.list
%doc asterisk-extra-sounds-en-g729-%{en_version}.list

%files en-gsm -f asterisk-extra-sounds-en-gsm-%{en_version}.list
%doc asterisk-extra-sounds-en-gsm-%{en_version}.list

%files en-siren7 -f asterisk-extra-sounds-en-siren7-%{en_version}.list
%doc asterisk-extra-sounds-en-siren7-%{en_version}.list

%files en-siren14 -f asterisk-extra-sounds-en-siren14-%{en_version}.list
%doc asterisk-extra-sounds-en-gsm-%{en_version}.list

%files en-sln16 -f asterisk-extra-sounds-en-sln16-%{en_version}.list
%doc asterisk-extra-sounds-en-sln16-%{en_version}.list

%files en-ulaw -f asterisk-extra-sounds-en-ulaw-%{en_version}.list
%doc asterisk-extra-sounds-en-ulaw-%{en_version}.list

%files en-wav -f asterisk-extra-sounds-en-wav-%{en_version}.list
%doc asterisk-extra-sounds-en-wav-%{en_version}.list

%files fr
%doc fr/extra-sounds-fr.txt
%doc fr/CHANGES-asterisk-extra-fr-%{fr_version}
%doc fr/CREDITS-asterisk-extra-fr-%{fr_version}
%license fr/LICENSE-asterisk-extra-fr-%{fr_version}
%dir %{sounds_dir}/fr/
%dir %{sounds_dir}/fr/ha/
%dir %{sounds_dir}/fr/wx/

%files fr-alaw -f asterisk-extra-sounds-fr-alaw-%{fr_version}.list
%doc asterisk-extra-sounds-fr-alaw-%{fr_version}.list

%files fr-g722 -f asterisk-extra-sounds-fr-g722-%{fr_version}.list
%doc asterisk-extra-sounds-fr-g722-%{fr_version}.list

%files fr-g729 -f asterisk-extra-sounds-fr-g729-%{fr_version}.list
%doc asterisk-extra-sounds-fr-g729-%{fr_version}.list

%files fr-gsm -f asterisk-extra-sounds-fr-gsm-%{fr_version}.list
%doc asterisk-extra-sounds-fr-gsm-%{fr_version}.list

%files fr-siren7 -f asterisk-extra-sounds-fr-siren7-%{fr_version}.list
%doc asterisk-extra-sounds-fr-siren7-%{fr_version}.list

%files fr-siren14 -f asterisk-extra-sounds-fr-siren14-%{fr_version}.list
%doc asterisk-extra-sounds-fr-siren14-%{fr_version}.list

%files fr-sln16 -f asterisk-extra-sounds-fr-sln16-%{fr_version}.list
%doc asterisk-extra-sounds-fr-sln16-%{fr_version}.list

%files fr-ulaw -f asterisk-extra-sounds-fr-ulaw-%{fr_version}.list
%doc asterisk-extra-sounds-fr-ulaw-%{fr_version}.list

%files fr-wav -f asterisk-extra-sounds-fr-wav-%{fr_version}.list
%doc asterisk-extra-sounds-fr-wav-%{fr_version}.list

%files en_GB
%doc en_GB/extra-sounds-en_GB.txt
%doc en_GB/CHANGES-asterisk-extra-en_GB-%{en_GB_version}
%doc en_GB/CREDITS-asterisk-extra-en_GB-%{en_GB_version}
%license en_GB/LICENSE-asterisk-extra-en_GB-%{en_GB_version}
%dir %{sounds_dir}/en_GB/

%files en_GB-alaw -f asterisk-extra-sounds-en_GB-alaw-%{en_GB_version}.list
%doc asterisk-extra-sounds-en_GB-alaw-%{en_GB_version}.list

%files en_GB-g722 -f asterisk-extra-sounds-en_GB-g722-%{en_GB_version}.list
%doc asterisk-extra-sounds-en_GB-g722-%{en_GB_version}.list

%files en_GB-g729 -f asterisk-extra-sounds-en_GB-g729-%{en_GB_version}.list
%doc asterisk-extra-sounds-en_GB-g729-%{en_GB_version}.list

%files en_GB-gsm -f asterisk-extra-sounds-en_GB-gsm-%{en_GB_version}.list
%doc asterisk-extra-sounds-en_GB-gsm-%{en_GB_version}.list

%files en_GB-siren7 -f asterisk-extra-sounds-en_GB-siren7-%{en_GB_version}.list
%doc asterisk-extra-sounds-en_GB-siren7-%{en_GB_version}.list

%files en_GB-siren14 -f asterisk-extra-sounds-en_GB-siren14-%{en_GB_version}.list
%doc asterisk-extra-sounds-en_GB-siren14-%{en_GB_version}.list

%files en_GB-sln16 -f asterisk-extra-sounds-en_GB-sln16-%{en_GB_version}.list
%doc asterisk-extra-sounds-en_GB-sln16-%{en_GB_version}.list

%files en_GB-ulaw -f asterisk-extra-sounds-en_GB-ulaw-%{en_GB_version}.list
%doc asterisk-extra-sounds-en_GB-ulaw-%{en_GB_version}.list

%files en_GB-wav -f asterisk-extra-sounds-en_GB-wav-%{en_GB_version}.list
%doc asterisk-extra-sounds-en_GB-wav-%{en_GB_version}.list

%changelog
* Fri Dec 27 2024 Luis Leal <Luis Leal> - 1.5.2-1
- Initial extra sounds packages

