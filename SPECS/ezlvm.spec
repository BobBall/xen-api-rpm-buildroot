# -*- rpm-spec -*-

Summary: Simple LVM storage adapter for xapi
Name:    ezlvm
Version: 0.3
Release: 1%{?dist}
License: LGPL
URL:     https://github.com/xapi-project/ezlvm
Source0: https://github.com/xapi-project/ezlvm/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: ocaml
BuildRequires: ocaml-camlp4-devel
BuildRequires: ocaml-findlib
BuildRequires: ocaml-findlib-devel
BuildRequires: xapi-storage-devel
BuildRequires: xapi-storage
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-uri-devel
BuildRequires: ocamlscript
BuildRequires: ocaml-ounit-devel
Requires: ocaml
Requires: ocaml-camlp4-devel
Requires: ocaml-findlib
Requires: ocaml-findlib-devel
Requires: xapi-storage-devel
Requires: xapi-storage
Requires: ocaml-re-devel
Requires: ocaml-cmdliner-devel
Requires: ocaml-uri-devel
Requires: ocamlscript
Requires: ocaml-ounit-devel

%description
Simple LVM storage adapter for xapi

%prep 
%setup -q -n %{name}-%{version}

%build
./volume/SR.ls --help=groff

%install
cd volume
DESTDIR=%{buildroot} SCRIPTDIR=%{_libexecdir}/xapi-storage-script/volume/org.xen.xcp.storage.ezlvm make install
cd ../datapath
DESTDIR=%{buildroot} SCRIPTDIR=%{_libexecdir}/xapi-storage-script/datapath/block make install

%files
%{_libexecdir}/xapi-storage-script/volume/org.xen.xcp.storage.ezlvm/*
%{_libexecdir}/xapi-storage-script/datapath/block/*

%changelog
* Tue Dec 23 2014 David Scott <dave.scott@citrix.com> - 0.3-1
- Update to 0.3

* Sat Nov  1 2014 David Scott <dave.scott@citrix.com> - 0.2.1-1
- Update to 0.2.1

* Fri Oct 17 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
