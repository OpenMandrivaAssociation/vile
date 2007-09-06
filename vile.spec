%define name vile 
%define version 9.5r
%define release %mkrel 1

Summary: Vi compatible text editor 
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL+
Group: Editors
Source: ftp://invisible-island.net/vile/%{name}-9.5.tar.bz2
Patch0: vile-9.5a.patch
Patch1: vile-9.5b.patch
Patch2: vile-9.5c.patch
Patch3: vile-9.5d.patch
Patch4: vile-9.5e.patch
Patch5: vile-9.5f.patch
Patch6: vile-9.5g.patch
Patch7: vile-9.5h.patch
Patch8: vile-9.5i.patch
Patch9: vile-9.5j.patch
Patch10: vile-9.5k.patch
Patch11: vile-9.5l.patch
Patch12: vile-9.5m.patch
Patch13: vile-9.5n.patch
Patch14: vile-9.5o.patch
Patch15: vile-9.5p.patch
Patch16: vile-9.5q.patch
Patch17: vile-9.5r.patch
Patch100: vile-9.5-varargs.patch
Patch101: vile-9.5-64bit-fixes.patch
BuildRequires:	flex ncurses-devel
BuildRoot:%{_tmppath}/%{name}-build-%{version}
URL: http://invisible-island.net/vile/

%description
vile is a text editor which is extremely compatible with vi in terms
of "finger feel".  in addition, it has extended capabilities in many areas,
notably multi-file editing and viewing, key rebinding, real X window
system support, an optional embedded perl interpreter, and robust
support for non-Unix hosts.

%prep
%setup -q -n %{name}-9.5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch100 -p1 -b .varargs
%patch101 -p1 -b .64bit-fixes

%build
%configure
%make prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

#(peroyvind) remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}.hlp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README doc/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_libdir}/%{name}
