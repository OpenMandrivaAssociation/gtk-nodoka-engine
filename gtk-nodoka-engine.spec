%define gtk2version %(pkg-config gtk+-2.0 --modversion 2> /dev/null)
%define nogtk2 %(pkg-config gtk+-2.0 --modversion &> /dev/null; echo $?)

Name:           gtk-nodoka-engine
Version:        0.7.5
Release:        2
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


%changelog
* Fri Oct 22 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7.5-1mdv2011.0
+ Revision: 587217
- Update to 0.7.5
- Use actual source url
- Split the extra themes in a noarch package (Fedora). And make it suggested by
  the main package
- Clean spec

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.7.2-2mdv2010.0
+ Revision: 437831
- rebuild

* Thu Dec 18 2008 Jérôme Soyer <saispo@mandriva.org> 0.7.2-1mdv2009.1
+ Revision: 315550
- New release 0.7.2

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6-3mdv2009.0
+ Revision: 246702
- rebuild

* Sun Dec 16 2007 Jérôme Soyer <saispo@mandriva.org> 0.6-1mdv2008.1
+ Revision: 120637
- Fix RPM Groups
- import gtk-nodoka-engine


