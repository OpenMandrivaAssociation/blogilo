Summary:	KDE blogging client
Name:		blogilo
Version:	17.04.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Blog)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5WebEngineViewer)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(KPimGAPI)
BuildRequires:	boost-devel
Requires:	kdepim-runtime
Conflicts:	blogilo < 3:16.08.3-4

%description
Blogilo is a blogging client for KDE, which supports famous blogging APIs.

%files -f %{name}.lang
%{_kde5_applicationsdir}/org.kde.blogilo.desktop
%{_kde5_bindir}/blogilo
%{_kde5_bindir}/composerhtmleditor
%{_kde5_datadir}/composereditorwebengine/composereditorinitialhtml
%{_kde5_datadir}/config.kcfg/blogilo.kcfg
%{_kde5_datadir}/kconf_update/blogilo*
%{_kde5_docdir}/*/*/blogilo
%{_kde5_iconsdir}/hicolor/*/actions/format-text-blockquote.*
%{_kde5_iconsdir}/hicolor/*/actions/format-text-code.*
%{_kde5_iconsdir}/hicolor/*/actions/insert-more-mark.*
%{_kde5_iconsdir}/hicolor/*/actions/remove-link.*
%{_kde5_iconsdir}/hicolor/*/actions/upload-media.*
%{_kde5_iconsdir}/hicolor/*/apps/blogilo.*
%{_kde5_sysconfdir}/xdg/blogilo.categories
%{_kde5_sysconfdir}/xdg/blogilo.renamecategories
%{_kde5_xmlguidir}/composerhtmleditor/composerhtmleditorui.rc
%{_datadir}/metainfo//org.kde.blogilo.appdata.xml

#----------------------------------------------------------------------------

%define composereditorwebengineprivate_major 5
%define libcomposereditorwebengineprivate %mklibname composereditorwebengineprivate %{composereditorwebengineprivate_major}

%package -n %{libcomposereditorwebengineprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libcomposereditorwebengineprivate}
KDE PIM shared library.

%files -n %{libcomposereditorwebengineprivate}
%{_kde5_libdir}/libcomposereditorwebengineprivate.so.%{composereditorwebengineprivate_major}*

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
%find_lang libcomposereditorwebengine
cat *.lang >%{name}.lang
