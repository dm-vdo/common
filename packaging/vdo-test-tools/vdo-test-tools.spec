%define repo_branch main

Name: vdo-test-tools
Version: 1.0
Release: 2
Summary: VDO Test tools
License: GPL2+
URL:     https://github.com/dm-vdo/vdo-devel
Source0: %{url}/archive/refs/heads/main.tar.gz
BuildRequires: make
BuildRequires: gcc
BuildRequires: zlib-devel

%description
This package provides test utilities that are used in the VDO test environment

%prep
%autosetup -n vdo-devel-%{repo_branch}/src/c++/vdo/tools

%build
make

%install
%{__install} -d $RPM_BUILD_ROOT%{_bindir} -m 0755
%{__install} -m 0755 genDiscard $RPM_BUILD_ROOT%{_bindir}/genDiscard
%{__install} -m 0755 genDataBlocks $RPM_BUILD_ROOT%{_bindir}/genDataBlocks
%{__install} -m 0755 setReadOnly $RPM_BUILD_ROOT%{_bindir}/setReadOnly

%files
%defattr(-,root,root)
%{_bindir}/genDiscard
%{_bindir}/genDataBlocks
%{_bindir}/setReadOnly

%changelog
* Nov 11 2025 Chung Chung <cchung@redhat.com> - 1.0-1
- Update description and inital push to github.

* Tue May 27 2025 Andy Walsh <awalsh@redhat.com> - 1.0-1
- Initial version
