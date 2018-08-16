%{!?upstream_version: %global upstream_version %{commit}}
%global commit 189b22ba3cc15024cc77a0e6acd10c44fefb2679
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-auditd
Version:                2.2.0
Release:                3%{?alphatag}%{?dist}
Summary:                Manage the audit daemon and it's rules.
License:                BSD

URL:                    https://github.com/kemra102/puppet-auditd

Source0:                https://github.com/kemra102/puppet-auditd/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 2.2.0-3.189b22bgit
- Update to post 2.2.0 (189b22ba3cc15024cc77a0e6acd10c44fefb2679)


