%define name vile 
%define version 9.5
%define lversion 9.2
%define serial z
%define release 2mdk

Summary: Vi compatible text editor 
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Editors
Source: %{name}-%{version}.tar.bz2
Patch0: vile-9.5-varargs.patch.bz2
Patch1: vile-9.5-64bit-fixes.patch.bz2
BuildRequires:	flex ncurses-devel
BuildRoot:%{_tmppath}/%{name}-build-%{version}
URL: http://www.vile.cx/

%description
vile is a text editor which is extremely compatible with vi in terms
of "finger feel".  in addition, it has extended capabilities in many areas,
notably multi-file editing and viewing, key rebinding, real X window
system support, an optional embedded perl interpreter, and robust
support for non-Unix hosts.

%prep
%setup -q
%patch0 -p1 -b .varargs
%patch1 -p1 -b .64bit-fixes

%build
%configure
%make prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mv $RPM_BUILD_ROOT/%{_mandir}/vile.1 $RPM_BUILD_ROOT/%{_mandir}/man1

#(peroyvind) remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}.hlp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README doc/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/*.rc
%{_datadir}/*.keywords
