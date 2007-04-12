%define libxp %mklibname xp 6
Name: libxp
Summary:  X Print Library
Version: 1.0.0
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
libXp provides public APIs to allow client applications to render to 
non-display devices.

#-----------------------------------------------------------

%package -n %{libxp}
Summary:  X Print Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxp}
libXp provides public APIs to allow client applications to render to 
non-display devices.

#-----------------------------------------------------------

%package -n %{libxp}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxp} = %{version}
Requires: x11-proto-devel >= 1.0.0

Conflicts: libxorg-x11-devel < 7.0
Provides: libxp-devel = %{version}-%{release}

%description -n %{libxp}-devel
Development files for %{name}

%files -n %{libxp}-devel
%defattr(-,root,root)
%{_libdir}/libXp.so
%{_libdir}/libXp.la
%{_libdir}/pkgconfig/xp.pc
%{_mandir}/man3/Xp*.3x.bz2
%{_mandir}/man3/libXp.3x.bz2

#-----------------------------------------------------------

%package -n %{libxp}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxp}-devel = %{version}
Provides: libxp-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxp}-static-devel
Static development files for %{name}

%files -n %{libxp}-static-devel
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxp}
%defattr(-,root,root)
%{_libdir}/libXp.so.6
%{_libdir}/libXp.so.6.2.0


