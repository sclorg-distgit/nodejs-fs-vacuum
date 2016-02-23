%{?scl:%scl_package nodejs-fs-vacuum}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-fs-vacuum

%global npm_name fs-vacuum
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
# Tests turned off due to missing dependencies

Name:		%{?scl_prefix}nodejs-fs-vacuum
Version:	1.2.6
Release:	4%{?dist}
Summary:	Recursively remove empty directories -- to a point
Url:		https://github.com/npm/fs-vacuum
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(mkdirp)
BuildRequires:	%{?scl_prefix}npm(tap)
BuildRequires:	%{?scl_prefix}npm(tmp)
%endif

BuildRequires:	%{?scl_prefix}npm(graceful-fs)
BuildRequires:	%{?scl_prefix}npm(path-is-inside)
BuildRequires:	%{?scl_prefix}npm(rimraf)

%description
Recursively remove empty directories -- to a point

%prep
%setup -q -n package

%nodejs_fixdep graceful-fs
%nodejs_fixdep path-is-inside
%nodejs_fixdep rimraf

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json vacuum.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/fs-vacuum

%doc README.md LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.6-4
- rebuilt

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.2.6-3
- Enable scl macros

* Tue Jul 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.6-2
- Added %%nodejs_fixdep macros

* Mon Jul 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.6-1
- New upstream release
- updated spec file
- added %%license

* Thu May 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com>- 1.2.5-1
- Initial build
