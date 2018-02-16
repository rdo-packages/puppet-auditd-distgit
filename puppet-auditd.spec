%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-auditd
%global commit c0c1ccb971dba3c085099ac3b012523f6c6b52a9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-auditd
Version:                2.2.0
Release:                2%{?alphatag}%{?dist}
Summary:                Manage the audit daemon and it's rules.
License:                BSD

URL:                    https://github.com/kemra102/puppet-auditd

Source0:                https://github.com/kemra102/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet-concat

Requires:               puppet >= 2.7.0

%description
This module handles installation of the auditd daemon, manages its main
configuration file as well as the user specified rules that auditd uses.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/auditd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/auditd/



%files
%{_datadir}/openstack-puppet/modules/auditd/


%changelog
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 2.2.0-2.c0c1ccbgit
- Update to post 2.2.0 (c0c1ccb971dba3c085099ac3b012523f6c6b52a9)

