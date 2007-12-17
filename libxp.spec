%define name	libxp
%define version	1.0.0
%define release	%mkrel 4

%define major		6
%define libname		%mklibname xp %{major}
%define develname	%mklibname xp -d
%define staticname	%mklibname xp -d -s

Name: %{name}
Summary:  X Print Library
Version: %{version}
Release: %{release}
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXp-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
libXp provides public APIs to allow client applications to render to 
non-display devices.

#-----------------------------------------------------------

%package -n %{libname}
Summary:  X Print Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
libXp provides public APIs to allow client applications to render to 
non-display devices.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Requires: x11-proto-devel >= 1.0.0
Conflicts: libxorg-x11-devel < 7.0
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname xp 6 -d}

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXp.so
%{_libdir}/libXp.la
%{_libdir}/pkgconfig/xp.pc
%{_mandir}/man3/Xp*.3*
%{_mandir}/man3/libXp.3*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %{mklibname xp 6 -d -s}

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXp.a

#-----------------------------------------------------------

%prep
%setup -q -n libXp-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXp.so.%{major}*

