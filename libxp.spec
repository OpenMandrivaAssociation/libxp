%define	major	6
%define	libname	%mklibname xp %{major}
%define	devname	%mklibname xp -d
%define	static	%mklibname xp -d -s

Name:		libxp
Summary:	X Print Library
Version:	1.0.1
Release:	5
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXp-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xau) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
libXp provides public APIs to allow client applications to render to
non-display devices.

#-----------------------------------------------------------

%package -n	%{libname}
Summary:	X Print Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
libXp provides public APIs to allow client applications to render to
non-display devices.

#-----------------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Requires:	x11-proto-devel >= 1.0.0
Conflicts:	libxorg-x11-devel < 7.0
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname xp 6 -d}

%description -n	%{devname}
Development files for %{name}

%files -n	%{devname}
%{_libdir}/libXp.so
%{_libdir}/pkgconfig/xp.pc
%{_mandir}/man3/Xp*.3*
%{_mandir}/man3/libXp.3*

#-----------------------------------------------------------

%package -n	%{static}
Summary:	Static development files for %{name}
Group:		Development/X11
Requires:	%{devname} = %{version}
Provides:	%{name}-static-devel = %{version}-%{release}
Conflicts:	libxorg-x11-static-devel < 7.0
Obsoletes:	%{mklibname xp 6 -d -s}

%description -n	%{static}
Static development files for %{name}

%files -n	%{static}
%{_libdir}/libXp.*a

#-----------------------------------------------------------

%prep
%setup -q -n libXp-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXp.so.%{major}*

%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2011.0
+ Revision: 661559
- mass rebuild

* Fri Jan 14 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.1-1
+ Revision: 631051
- New version: 1.0.1

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9mdv2011.0
+ Revision: 602622
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-8mdv2010.1
+ Revision: 520969
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.0-7mdv2010.0
+ Revision: 425931
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 223080
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.0-5mdv2008.1
+ Revision: 151689
- Update BuildRequires and rebuild.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 08 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-4mdv2008.0
+ Revision: 60440
- rebuild for 2008
- new devel policy
- spec clean


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

