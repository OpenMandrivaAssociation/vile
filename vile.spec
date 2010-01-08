Summary:	Mostly vi-compatible text editor, with enhancements
Name:		vile
Version:	9.7z
Release:	%mkrel 2
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
