%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Violetto theme for the GRUB bootloader
Name:		violetto-grub
Version:	2.0.1
Release:	1
License:	GPL
Group:		Graphical desktop/KDE
Url:		https://github.com/rugyada/violetto-grub
Source0:	%{name}-%version.tar.gz
Requires:	grub2
BuildArch:	noarch

%description
Violetto theme for the GRUB bootloader

%files
/boot/grub2/themes/violetto-grub

%prep
%autosetup

%build
# nothing

%install
mkdir -p %{buildroot}/boot/grub2/themes
cp -a violetto-grub %{buildroot}/boot/grub2/themes/
