Summary:	Mostly vi-compatible text editor, with enhancements
Name:		vile
Version:	9.8
Release:	%mkrel 1
License:	GPL+
Group:		Editors
Source0:	ftp://invisible-island.net/vile/current/%{name}-%{version}.tgz
Patch101:	vile-9.5-64bit-fixes.patch
BuildRequires:	flex
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-build-%{version}
URL:		http://invisible-island.net/vile/

%description
vile is a text editor which is extremely compatible with vi in terms
of "finger feel".  in addition, it has extended capabilities in many areas,
notably multi-file editing and viewing, key rebinding, real X window
system support, an optional embedded perl interpreter, and robust
support for non-Unix hosts.

%prep
%setup -q 
%patch101 -p1 -b .64bit-fixes

%build
%configure2_5x
%make prefix=%{_prefix}

%install
rm -rf %{buildroot}

%makeinstall_std

#(peroyvind) remove unpackaged files
rm -f %{buildroot}%{_datadir}/%{name}.hlp

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README doc/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_libdir}/%{name}


%changelog
* Mon Aug 09 2010 Funda Wang <fwang@mandriva.org> 9.8-1mdv2011.0
+ Revision: 567863
- new version 9.8

* Fri Jan 08 2010 Frederik Himpe <fhimpe@mandriva.org> 9.7z-2mdv2010.1
+ Revision: 487765
- Really update to version 9.7z
- Remove old patches

* Fri Jan 08 2010 Frederik Himpe <fhimpe@mandriva.org> 9.7z-1mdv2010.1
+ Revision: 487755
- update to new version 9.7z

* Fri Nov 20 2009 Frederik Himpe <fhimpe@mandriva.org> 9.7x-1mdv2010.1
+ Revision: 467661
- update to new version 9.7x

* Tue Aug 25 2009 Frederik Himpe <fhimpe@mandriva.org> 9.7u-1mdv2010.0
+ Revision: 421220
- update to new version 9.7u

* Mon Jul 20 2009 Frederik Himpe <fhimpe@mandriva.org> 9.7t-1mdv2010.0
+ Revision: 398118
- update to new version 9.7t

* Thu Jun 11 2009 Frederik Himpe <fhimpe@mandriva.org> 9.7s-1mdv2010.0
+ Revision: 385165
- update to new version 9.7s

* Wed May 27 2009 Frederik Himpe <fhimpe@mandriva.org> 9.7r-1mdv2010.0
+ Revision: 380277
- Use %%mkrel
- update to new version 9.7r

* Sun Oct 12 2008 Adam Williamson <awilliamson@mandriva.org> 9.7e-1mdv2009.1
+ Revision: 292593
- add definitions.patch to fix some apparently missing defines that broke build
- new version 9.7 (patch level e)

* Sat Mar 01 2008 Adam Williamson <awilliamson@mandriva.org> 9.6g-1mdv2008.1
+ Revision: 177117
- minor spec clean
- use vanilla upstream sources
- new release 9.6, patchlevel g

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 9.5r-1mdv2008.0
+ Revision: 80601
- use Fedora license policy
- renumber patches so we don't have to keep changing the number of the mdv patches
- new patch 9.5r

* Thu May 31 2007 Adam Williamson <awilliamson@mandriva.org> 9.5q-1mdv2008.0
+ Revision: 33280
- fix patch
- correct URL
- adapt patch from Trent Piepho to fix #22226 (install location)
- reorder patches, rediff varargs patch
- update to patch level Q
- Import vile



* Tue Aug 23 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 9.5-2mdk
- varargs & 64-bit fixes

* Thu Aug 18 2005 Daouda LO <daouda@mandriva.com> 9.5-1mdk
- 9.5
- several new majormodes, with corresponding syntax filters 
  (jsp, nmakemode, lispmode ...)

* Wed Dec 17 2003 Daouda LO <daouda@mandrakesoft.com> 9.4-1mdk
- 9.4 

* Thu Jun 05 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 9.3-2mdk
- fix unpackaged files
- macroize

* Fri Jul  5 2002 Daouda LO <daouda@mandrakesoft.com> 9.3-1mdk
- 9.3
- patches streamlined

* Thu Apr 11 2002 Daouda LO <daouda@mandrakesoft.com> 9.2-11mdk
- release: patch n <-> z

* Sun Sep 09 2001 Stefan van der Eijk <stefan@eijk.nu> 9.2-10mdk
- BuildRequires: flex ncurses-devel

* Thu Jun 14 2001 Daouda Lo <daouda@mandrakesoft.com> 9.2-9mdk
- release : patch n

* Fri May  25 2001  Daouda Lo <daouda@mandrakesoft.com> 9.2-8mdk
- release: applied patch j to m

* Tue Mar  6 2001  Daouda Lo <daouda@mandrakesoft.com> 9.2-7mdk
- release: applied patch i

* Mon Feb 26 2001  Daouda Lo <daouda@mandrakesoft.com> 9.2-6mdk
- 9.2e -> 9.2h patches applied 

* Wed Feb 14 2001 Lenny Cartier <lenny@mandrakesoft.com> 9.2-5mdk
- fix group (thx yves)

* Wed Feb 14 2001 Lenny Cartier <lenny@mandrakesoft.com> 9.2-4mdk
- rebuild
- add url

* Thu Dec  7 2000  Daouda Lo<daouda@mandrakesoft.com> 9.2-3mdk
- 9.2d (bug fixes + cleanup)

* Thu Nov 16 2000 Daouda Lo <daouda@mandrakesoft.com> 9.2-2mdk
- 9.2c release (3 patches to 9.2)
- more macros 
- fixed package that owned standard dir.
- gcc 2.96 build

* Fri Oct 27 2000 Daouda Lo <daouda@mandrakesoft.com> 9.2-1mdk
- new release

* Thu Sep 28 2000 Florin Grad <florin@mandrakesoft.com> 9.1-1mdk
- first attempt
