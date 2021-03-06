%define abiquo_basedir /opt/abiquo

Name:     abiquo-ssm
Version:  3.0.0
Release:  3%{?dist}%{?buildstamp}
Summary:  Abiquo System Storage Manager
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  %{?abiquo_binaries_url}ssm.war
Source1:  %{?abiquo_binaries_url}scripts/nfs-plugin
Source2:  %{?abiquo_binaries_url}scripts/nfs-plugin-test
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core bc qemu-img
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package contains the enterprise ssm component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/ssm/ %{SOURCE0}

mkdir -p %{buildroot}/%{_bindir}
%{__install} -Dp -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}
%{__install} -Dp -m 0755 %{SOURCE2} %{buildroot}/%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tomcat/webapps/ssm
%{_bindir}/nfs-plugin
%{_bindir}/nfs-plugin-test

%changelog
* Thu Feb 06 2014 Abel Boldú <abel.boldu@abiquo.com> - 3.0.0-3
- Bumped version to 3.0.0, added nfs plugins.

* Fri Nov 15 2013 Abel Boldú <abel.boldu@abiquo.com> - 2.7.0-1
- Bumped version to 2.7.0

* Fri Nov 08 2013 Abel Boldú <abel.boldu@abiquo.com> - 2.6.2-1
- Bumped version to 2.6.2

* Mon Oct 21 2013 Abel Boldú <abel.boldu@abiquo.com> - 2.6.1-1
- Bumped version to 2.6.1

* Thu Jul 25 2013 Abel Boldú <abel.boldu@abiquo.com> - 2.6.0-4
- New requirements added.

* Wed Jul 24 2013 Abel Boldú <abel.boldu@abiquo.com> - 2.6.0-3
- NFS plugin scripts added.

* Tue Apr 23 2013 Abel Boldú <abel.boldu@abiquo.com> - 2.6.0-2
- Bumped version to 2.6.0

* Wed Dec 05 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.4.0-1
- Bumped version to 2.4.0

* Tue Oct 23 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.3.0-1
- bumped version to 2.3.0

* Fri Aug 31 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.2.0-1
- new versioning

* Fri Jun 08 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.2-1
- Bumped version to 2.2

* Thu Apr 19 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.0-3
- 2.0-HF1 bump

* Mon Dec 19 2011 Sergio Rubio <srubio@abiquo.com> - 2.0-2
- bumped version to 2.0

* Fri Sep 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-1
- bumped version to 1.8.5

* Mon May 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-1
- updated to 1.8

* Thu Apr 14 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.6-1
- bumped version

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- version bump

* Mon Feb 28 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-7
- set buildarch to noarch

* Wed Feb 16 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6
- fix release string

* Thu Feb 03 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5.GA
- upstream fixes

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4.GA
- GA build

* Mon Jan 10 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- use the ssm WAR as Source0

* Tue Dec 14 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- use the new build system

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Thu Sep 02 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.5

* Fri Jul 09 2010 Sergio Rubio srubio@abiquo.com 1.6-2
- Added buildstamp to the package

* Mon Jul 05 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Updated to upstream 1.6

* Wed May 26 2010 Sergio Rubio srubio@abiquo.com 1.5.1
- Initial Release
