%define major	2
%define api	1.0

%define libname %mklibname ideviceactivation %{api} %{major}
%define devname %mklibname -d ideviceactivation

%define	git	20211124

Summary:	Library to manage the activation of iOS device
Name:		libideviceactivation
Version:	1.1.2
Release:	1.%{git}.0
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(libimobiledevice)
BuildRequires:	pkgconfig(libimobiledevice-glue)
BuildRequires:	pkgconfig(libplist)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml2)

%description
Provides an interface to activate and deactivate iOS devices by
talking to Apple's webservice. 
A command-line utility ideviceactivation is also available


%package -n %{libname}
Group:		System/Libraries
Summary:	Library to manage the activation of iOS devices
Suggests:	%{name} >= %{version}-%{release}

%description -n %{libname}
Library to manage the activation of iOS devices

%package -n %{devname}
Summary:	Development package for libirecovery
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name}, development headers and libraries.


%package -n ideviceactivation
Group:          System/Tools
Summary:        Tool to access iboot/iBSS over usb on IOS devices
Requires:       %{libname} = %{version}-%{release}

%description -n ideviceactivation
ideviceactivation is a system tool which can be used to activate or deactivate iOS devices

%prep
%autosetup -p1

%build
autoreconf -fiv

%configure \
	--disable-static

%make_build

%install
%make_install

%files 
%doc NEWS README.md COPYING

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}-%{api}.so

%files -n ideviceactivation
%{_bindir}/ideviceactivation
%{_mandir}/man1/*

