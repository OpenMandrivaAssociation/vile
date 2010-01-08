Summary:	Mostly vi-compatible text editor, with enhancements
Name:		vile
Version:	9.7z
Release:	%mkrel 1
License:	GPL+
Group:		Editors
Source0:	ftp://invisible-island.net/vile/%{name}-9.7.tgz
Patch0:		ftp://invisible-island.net/vile/patches/vile-9.7a.patch.gz
Patch1:		ftp://invisible-island.net/vile/patches/vile-9.7b.patch.gz
Patch2:		ftp://invisible-island.net/vile/patches/vile-9.7c.patch.gz
Patch3:		ftp://invisible-island.net/vile/patches/vile-9.7d.patch.gz
Patch4:		ftp://invisible-island.net/vile/patches/vile-9.7e.patch.gz
Patch100:	vile-9.5-varargs.patch
Patch101:	vile-9.5-64bit-fixes.patch
Patch102:	vile-9.7-definitions.patch
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
%setup -q -n %{name}-9.7
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch100 -p1 -b .varargs
%patch101 -p1 -b .64bit-fixes
%patch102 -p1 -b .one_line

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
