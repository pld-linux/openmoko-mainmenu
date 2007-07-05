#
Summary:	OpenMoko main menu applet
Name:		openmoko-mainmenu
Version:	0.0.0.2352
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	18cfbbe6e6f1710c24377fb0bf8371b1
URL:		http://openmoko.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libmatchbox-devel >= 1.8
BuildRequires:	openmoko-libs-devel
Requires:	openmoko-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define openmokoname %(echo %{name} | sed -e 's/openmoko-//')

%description
OpenMoko main menu applet

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/openmoko-mainmenu
%{_desktopdir}/openmoko-mainmenu.desktop
%dir %{_datadir}/openmoko-mainmenu
%{_datadir}/openmoko-mainmenu/*.png
%{_datadir}/openmoko-mainmenu/*.xpm
%{_pixmapsdir}/openmoko-mainmenu.png
