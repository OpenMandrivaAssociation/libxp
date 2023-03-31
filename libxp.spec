%define major 6
%define libname %mklibname xp %{major}
%define devname %mklibname xp -d
%define static %mklibname xp -d -s

Name:		libxp
Summary:	X Print Library
Version:	1.0.4
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXp-%{version}.tar.xz

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xau) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
libXp provides public APIs to allow client applications to render to
non-display devices.

%package -n	%{libname}
Summary:	X Print Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
libXp provides public APIs to allow client applications to render to
non-display devices.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Requires:	x11-proto-devel >= 1.0.0
Conflicts:	libxorg-x11-devel < 7.0
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname xp 6 -d}

%description -n	%{devname}
Development files for %{name}.

%package -n	%{static}
Summary:	Static development files for %{name}
Group:		Development/X11
Requires:	%{devname} = %{version}
Provides:	%{name}-static-devel = %{version}-%{release}
Conflicts:	libxorg-x11-static-devel < 7.0
Obsoletes:	%{mklibname xp 6 -d -s}

%description -n	%{static}
Static development files for %{name}.

%prep
%autosetup -p1 -n libXp-%{version}

%build
%configure \
		--enable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libXp.so.%{major}*

%files -n %{devname}
%{_libdir}/libXp.so
%{_libdir}/pkgconfig/xp.pc
%{_mandir}/man3/Xp*.3*
%{_mandir}/man3/libXp.3*

%files -n %{static}
%{_libdir}/libXp.*a
