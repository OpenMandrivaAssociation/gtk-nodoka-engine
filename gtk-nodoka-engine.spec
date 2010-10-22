%define gtk2version %(pkg-config gtk+-2.0 --modversion 2> /dev/null)
%define nogtk2 %(pkg-config gtk+-2.0 --modversion &> /dev/null; echo $?)

Name:           gtk-nodoka-engine
Version:        0.7.5
Release:        %mkrel 1
Summary:        The Nodoka GTK Theme Engine
Group:          Graphical desktop/GNOME
License:        GPLv2
URL:            http://fedoraproject.org/wiki/Artwork/NodokaTheme
Source0:        https://fedorahosted.org/released/nodoka/%{name}-%{version}.tar.gz
BuildRequires:  gtk2-devel >= 2.18
%if 0%{?nogtk2}
Requires:       gtk2
%else
Requires:       gtk2 >= %{?gtk2version}
%endif
Provides:       gtk2-nodoka-engine = %{version}-%{release}
Suggests:       gtk-nodoka-engine-extras

%description
Nodoka is a Murrine engine based gtk2 theme engine. The package is shipped with
a default Nodoka theme featuring the engine.

%package extras
Summary:   Extra themes for Nodoka Gtk2 theme engine
Group:     Graphical desktop/GNOME
Requires:  %{name} >= 0.6.90.1
Provides:  gtk2-nodoka-engine-extras = %{version}-%{release}
BuildArch: noarch

%description extras
This package contains extra themes for the Nodoka Gtk2 theme engine.

%prep
%setup -q

%build
%configure2_5x --with-gtk=2.0
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#remove .la files
find %{buildroot} -name *.la | xargs rm -f

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README TODO
%{_libdir}/gtk-2.0/2.10.0/engines/libnodoka.so
%{_datadir}/themes/Nodoka

%files extras
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/themes/Nodoka-*
