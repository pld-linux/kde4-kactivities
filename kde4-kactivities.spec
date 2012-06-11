%define		_state		stable
%define		orgname		kactivities
%define		qtver		4.8.1

Summary:	K Desktop Environment - a C++ library for using Nepomuk activities
Summary(pl.UTF-8):	K Desktop Environment - Biblioteka C++ do aktywności Nepomuka
Name:		kde4-kactivities
Version:	4.8.4
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	bcbd686884c3afb020ec3da9c422e60a
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	soprano-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++ library for using Nepomuk activities.

%description -l pl.UTF-8
Biblioteka C++ do aktywności Nepomuka.

%package devel
Summary:	kactivities development files
Summary(pl.UTF-8):	Pliki dla programistów kactivities
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
kactivities development files.

%description devel -l pl.UTF-8
Pliki dla programistów kactivities.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kactivitymanagerd
%attr(755,root,root) %{_libdir}/libkactivities.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkactivities.so.?
%attr(755,root,root) %{_libdir}/kde4/activitymanager_plugin_dummy.so
%attr(755,root,root) %{_libdir}/kde4/activitymanager_plugin_globalshortcuts.so
%attr(755,root,root) %{_libdir}/kde4/activitymanager_plugin_nepomuk.so
%attr(755,root,root) %{_libdir}/kde4/activitymanager_plugin_slc.so
%{_datadir}/kde4/services/activitymanager-plugin-dummy.desktop
%{_datadir}/kde4/services/activitymanager-plugin-globalshortcuts.desktop
%{_datadir}/kde4/services/activitymanager-plugin-nepomuk.desktop
%{_datadir}/kde4/services/activitymanager-plugin-slc.desktop
%{_datadir}/kde4/services/kactivitymanagerd.desktop
%{_datadir}/kde4/services/kded/activitymanager.desktop
%{_datadir}/kde4/servicetypes/activitymanager-plugin.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KDE/KActivities
%{_includedir}/kactivities
%{_libdir}/cmake/KActivities
%{_pkgconfigdir}/libkactivities.pc
%attr(755,root,root) %{_libdir}/libkactivities.so
