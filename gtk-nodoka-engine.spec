%define gtk2version %(pkg-config gtk+-2.0 --modversion 2> /dev/null)
%define nogtk2 %(pkg-config gtk+-2.0 --modversion &> /dev/null; echo $?)

Name:           gtk-nodoka-engine
Version:        0.6
Release:        %mkrel 1
Summary:        The Nodoka GTK Theme Engine

Group:          Graphical desktop/GNOME
License:        GPLv2
URL:            http://fedoraproject.org/wiki/Artwork/NodokaTheme
Source0:        gtk-nodoka-engine-%{version}.tar.gz
Patch0:         gtk-nodoka-engine-0.6-tooltips.patch
Patch1:         gtk-nodoka-engine-0.6-treeview.patch
Patch2:         gtk-nodoka-engine-0.6-gimp-crash.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  gtk2-devel
%if 0%{?nogtk2}
Requires:       gtk2
%else
Requires:       gtk2 >= %{?gtk2version}
%endif

%description
Nodoka is a Murrine engine based gtk2 theme engine. The package is shipped with
a default Nodoka theme featuring the engine.


%prep
%setup -q
%patch0 -p1 -b .tooltips
%patch1 -p1 -b .treeview
%patch2 -p1 -b .gimp-crash

%build
%configure2_5x
%make


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
%makeinstall_std

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README TODO
%{_libdir}/gtk-2.0/2.10.0/engines/libnodoka.so
%{_datadir}/themes/Nodoka
