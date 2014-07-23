%define debug_package %{nil}

Name:           xapi-quicktest
Version:        0.0.0
Release:        1%{?dist}
Summary:        Simple xapi-project test suite
License:        ISC
URL:            https://github.com/xapi-project/quicktest
Source0:        https://github.com/xapi-project/quicktest/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-testvmlib-devel
BuildRequires:  ocaml-vchan-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-xen-api-client-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  ocaml-gnt-devel
BuildRequires:  ocaml-evtchn-devel
BuildRequires:  ocaml-ipaddr-devel
%description
This is a simple test suite for the xapi-project components

%prep
%setup -q -n quicktest-%{version}

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
cp quicktest.native %{buildroot}%{_bindir}

%files
%doc README.md
%{_bindir}/quicktest.native

%changelog
* Wed Jul 23 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.0.0-1
- Initial package
