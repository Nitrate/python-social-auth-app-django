# Created by pyp2rpm-3.3.5
%global pypi_name social-auth-app-django

Name:           python-%{pypi_name}
Version:        3.4.0
Release:        1%{?dist}
Summary:        Python Social Authentication, Django integration

License:        BSD
URL:            https://github.com/python-social-auth/social-app-django
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(social-auth-core) >= 3.3.0

%description
Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(six)
Requires:       python3dist(social-auth-core) >= 3.3.0

%description -n python3-%{pypi_name}
Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# The sdist does not include this test data
mkdir tests/templates/
echo -n "test" > tests/templates/test.html
python3 manage.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/social_django
%{python3_sitelib}/social_auth_app_django-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Feb 11 2021 Chenxiong Qi <qcxhome@gmail.com> - 3.4.0-1
- Initial package.
