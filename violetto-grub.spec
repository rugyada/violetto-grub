Name:		violetto-grub
Version:	2.0
Release:	1
Summary:	Violetto theme for the GRUB bootloader
License:	GPL
Group:		Graphical desktop/KDE
Url:		https://github.com/rugyada/violetto-grub
Source0:	%{name}-%version.tar.gz
Requires:	grub2
BuildArch:	noarch

%description
This package contains Violetto theme for
the GRUB bootloader

%files
/boot/grub2/themes/violetto-grub

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/boot/grub2/themes
cp -a violetto-grub %{buildroot}/boot/grub2/themes/violetto
