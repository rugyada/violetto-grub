# Violetto grub theme
%define oname Violetto
%define bdate   2021.10.22

Summary:	Violetto theme for the GRUB bootloader
Name:		violetto-grub
Version:	2.0.1
Release:	1
License:	GPL
Group:		Graphical desktop/KDE
Url:		https://github.com/rugyada/violetto-grub
Source0:	%{oname}-%version.tar.gz
Requires:	grub2
BuildArch:	noarch

%description
Violetto theme for the GRUB bootloader

%files
/boot/grub2/themes/Violetto

%prep
%setup -qn %{oname}-%{version}

%build


%install
mkdir -p %{buildroot}/boot/grub2/themes/Violetto
cp * %{buildroot}/boot/grub2/themes/Violetto/
