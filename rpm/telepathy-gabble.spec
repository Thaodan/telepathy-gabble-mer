Name:       telepathy-gabble

Summary:    A Jabber/XMPP connection manager
Version:    0.18.3
Release:    1
Group:      Applications/Communications
License:    LGPLv2+ and BSD
URL:        http://telepathy.freedesktop.org/wiki/
Source0:    http://telepathy.freedesktop.org/releases/telepathy-gabble/%{name}-%{version}.tar.gz
Source1:    INSIGNIFICANT
Source2:    mktests.sh
Patch0:     nemo-tests-dir-fix.patch
Patch1:     0001-Disable-parallel-build-for-extensions-directory.patch
Patch2:     wocky-disable-gtkdoc.patch
Patch4:     0001-Change-default-keepalive-interval-to-2.5-minutes.patch
Requires:   telepathy-mission-control
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(dbus-1) >= 1.1.0
BuildRequires:  pkgconfig(nice) >= 0.0.11
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.82
BuildRequires:  pkgconfig(telepathy-glib) >= 0.19.9
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0) >= 2.32
BuildRequires:  pkgconfig(gthread-2.0) >= 2.32
BuildRequires:  pkgconfig(gio-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.32
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libiphb)
BuildRequires:  python
BuildRequires:  ca-certificates
BuildRequires:  python-twisted
BuildRequires:  dbus-python

%description
A Jabber/XMPP connection manager, that handles single and multi-user
chats and voice calls.





%prep
%setup -q -n %{name}-%{version}/%{name}

%patch0 -p1
# 0001-Disable-parallel-build-for-extensions-directory.patch
%patch1 -p1
# 0001-Change-default-keepalive-interval-to-2.5-minutes.patch
%patch4 -p1
cd lib/ext/wocky
%patch2 -p1



%build
# >> build pre
cd lib/ext/wocky
%autogen --no-configure --disable-gtk-doc
cd ../../..
%autogen --disable-submodules --no-configure
# << build pre

%reconfigure --disable-static \
    --disable-installed-tests

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc %{_datadir}/doc/%{name}/*.html
%{_libexecdir}/%{name}
%{_bindir}/telepathy-gabble-xmpp-console
%{_libdir}/telepathy/gabble-0/lib/libgabble-plugins-*.so
%{_libdir}/telepathy/gabble-0/lib/libgabble-plugins.so
%{_libdir}/telepathy/gabble-0/lib/libwocky-telepathy-gabble-*.so
%{_libdir}/telepathy/gabble-0/lib/libwocky.so
%{_libdir}/telepathy/gabble-0/plugins/libconsole.so
%{_libdir}/telepathy/gabble-0/plugins/libgateways.so
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_mandir}/man8/%{name}.8.gz
# << files


