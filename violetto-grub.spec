%define oname violetto
%define bdate   2021.10.22

Summary:	Violetto theme for the GRUB bootloader
Name:		violetto
Version:	2.0
Release:	1
License:	GPL
Group:		Graphical desktop/KDE
Url:		https://github.com/rugyada/violetto-grub
Source0:	violetto.tar.gz
Requires:	grub2
%endif
BuildArch:	noarch

%description
This package contains Violetto theme for
the GRUB bootloader

%files
/boot/grub2/themes/violetto

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/boot/grub2/themes
cp -a violetto %{buildroot}/boot/grub2/themes/
