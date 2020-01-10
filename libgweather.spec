Name:           libgweather
Version:        3.20.4
Release:        1%{?dist}
Summary:        A library for weather information

License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/LibGWeather
Source0:        https://download.gnome.org/sources/libgweather/3.20/%{name}-%{version}.tar.xz
Patch0:         libgweather-3.20.3-fix-includes.patch

BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.13.5
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.34
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gnome-common
BuildRequires:  vala-devel
BuildRequires:  vala

%description
libgweather is a library to access weather information from online
services for numerous locations.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static --disable-gtk-doc
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name} --all-name

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files -f %{name}.lang
%doc HACKING NEWS README
%license COPYING
%{_libdir}/libgweather-3.so.*
%{_libdir}/girepository-1.0/GWeather-3.0.typelib
%dir %{_datadir}/libgweather
%{_datadir}/libgweather/Locations.xml
%{_datadir}/libgweather/locations.dtd
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.gschema.xml

%files devel
%{_includedir}/libgweather-3.0
%{_libdir}/libgweather-3.so
%{_libdir}/pkgconfig/gweather-3.0.pc
%{_datadir}/gir-1.0/GWeather-3.0.gir
%dir %{_datadir}/glade/
%dir %{_datadir}/glade/catalogs/
%{_datadir}/glade/catalogs/libgweather.xml
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libgweather-3.0
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/gweather-3.0.vapi


%changelog
* Tue Dec 27 2016 Kalev Lember <klember@redhat.com> - 3.20.4-1
- Update to 3.20.4
- Resolves: #1387009

* Wed Aug 31 2016 Kalev Lember <klember@redhat.com> - 3.14.1-3
- Switch to new METAR data provider
- Resolves: #1371550

* Fri Jul  1 2016 Matthias Clasen <mclasen@redhat.com> - 3.14.1-2
- Update translations
  Resolves: #1304249

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1
- Resolves: #1174505

* Thu Sep 11 2014 Zeeshan Ali <zeenix@redhat.com> - 3.8.2-5
- yr.no API changes (related: #1139747).

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.2-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.2-3
- Mass rebuild 2013-12-27

* Mon Dec  2 2013 Zeeshan Ali <zeenix@redhat.com> - 3.8.2-2
- Complete translations (related: #1030365).

* Mon May 13 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Tue Nov 20 2012 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-2
- Silence glib-compile-schemas scriplets

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Tue Jun 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.1-1
- Update to 3.5.1

* Thu Jan 12 2012 Matthias Clasen <mclasen@redhat.com> - 3.2.1-2
- Drop gtk-doc dependency

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Mon Sep 26 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Mon Jul 04 2011 Bastien Nocera <bnocera@redhat.com> 3.1.3-1
- Update to 3.1.3

* Mon Apr  4 2011 Christopher Aillon <caillon@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-3
- Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Bastien Nocera <bnocera@redhat.com> 2.91.6-1
- Update to 2.91.6

* Sun Jan 30 2011 Matthew Barnes <mbarnes@redhat.com> - 2.91.0-1
- Update to 2.91.0

* Thu Sep 30 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.3-1
- Update to 2.30.3

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Tue Mar 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-1
- Update to 2.29.92

* Tue Feb 23 2010 Matthias Clasen <mclasen@redhat.com> 2.29.91-1
- Update to 2.29.91

* Wed Feb 10 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-1
- Update to 2.29.90

* Tue Jan 12 2010 Matthias Clasen <mclasen@redhat.com> 2.29.5-1
- Update to 2.29.5

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> 2.29.4-1
- Update to 2.29.4

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-1
- Update to 2.28.0

* Wed Sep  9 2009 Matthias Clasen <mclasen@redhat.com> 2.27.92-1
- Update to 2.27.92

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhat.com> 2.27.91-1
- Update to 2.27.91

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Matthias Clasen <mclasen@redhat.com> 2.26.1-5
- Keep locations in gettext catalogs

* Wed Jun 10 2009 Matthias Clasen <mclasen@redhat.com> 2.26.1-3
- Fix multilib parallel-installability (#477672)
- Remove some old optimizations that are now no-ops

* Mon Apr 27 2009 Matthias Clasen <mclasen@redhat.com> 2.26.1-2
- Don't drop schemas translations from po files

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/libgweather/2.26/libgweather-2.26.1.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> 2.26.0-1
- Update to 2.26.0

* Tue Mar  3 2009 Matthias Clasen <mclasen@redhat.com> 2.25.92-1
- Update to 2.25.92

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Clasen <mclasen@redhat.com> 2.25.91-1
- Update to 2.25.91

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> 2.25.5-1
- Upate to 2.25.5

* Mon Jan 05 2009 Matthew Barnes <mbarnes@redhat.com> 2.25.4-1
- Update to 2.25.4

* Tue Dec 16 2008 Matthias Clasen <mclasen@redhat.com> 2.25.3-2
- Update to 2.25.3

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> 2.25.2-2
- Update to 2.25.2

* Wed Oct 22 2008 Matthias Clasen <mclasen@redhat.com> 2.24.1-1
- Update to 2.24.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> 2.24.0-2
- Apply %%lang tags to localized xml files

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> 2.23.91-1
- Update to 2.23.91

* Mon Aug  4 2008 Matthias Clasen <mclasen@redhat.com> 2.23.6-1
- Update to 2.23.6

* Fri Jul 25 2008 Matthias Clasen <mclasen@redhat.com> 2.23.5-2
- Fix pending request accounting

* Tue Jul 22 2008 Matthias Clasen <mclasen@redhat.com> 2.23.5-1
- Update to 2.23.5

* Tue Jun 17 2008 Matthias Clasen <mclasen@redhat.com> 2.23.4-1
- Update to 2.23.4

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> 2.23.3-1
- Update to 2.23.3

* Wed May 14 2008 Matthias Clasen <mclasen@redhat.com> 2.23.2-1
- Update to 2.23.2

* Thu Apr 24 2008 Matthias Clasen <mclasen@redhat.com> 2.23.1-1
- Update to 2.23.1

* Thu Apr 17 2008 Matthias Clasen <mclasen@redhat.com> 2.22.1.1-2
- Leave Cairo in Africa (#442793)

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> 2.22.1.1-1
- Update to 2.22.1.1

* Tue Mar 11 2008 Matthias Clasen <mclasen@redhat.com> 2.22.0-1
- Update to 2.22.0

* Tue Feb 26 2008 Matthias Clasen <mclasen@redhat.com> 2.21.92-1
- Update to 2.21.92

* Mon Feb 11 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-6
- Remove obsolete translations

* Sat Feb  9 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-5
- Rebuild for gcc 4.3

* Wed Jan 16 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-4
- Add Obsoletes for gnome-applets-devel

* Wed Jan 16 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-3
- Carry over space-saving hack from gnome-applets

* Tue Jan 15 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-2
- Incorporate review feedback (#428739)

* Mon Jan 14 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-1
- Update to 2.21.2

* Thu Jan 10 2008  Matthias Clasen <mclasen@redhat.com> 2.21.1-1
- Initial packaging

