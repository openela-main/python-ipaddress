%global pyname ipaddress

Name:           python-%{pyname}
Version:        1.0.18
Release:        6%{?dist}
Summary:        Port of the python 3.3+ ipaddress module to 2.6+

License:        Python
URL:            https://pypi.python.org/pypi/ipaddress/
Source0:        https://pypi.python.org/packages/source/i/%{pyname}/%{pyname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%global _description\
ipaddress provides the capabilities to create, manipulate and operate\
on IPv4 and IPv6 addresses and networks.\
\
The functions and classes in this module make it straightforward to\
handle various tasks related to IP addresses, including checking\
whether or not two hosts are on the same subnet, iterating over all\
hosts in a particular subnet, checking whether or not a string\
represents a valid IP address or network definition, and so on.

%description %_description

%package -n python2-%{pyname}
Summary: %summary
%{?python_provide:%python_provide python2-%{pyname}}

%description -n python2-%{pyname} %_description

%prep
%setup -q -n %{pyname}-%{version}


%build
%{__python2} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files -n python2-%{pyname}
%doc README.md
%{python2_sitelib}/*


%changelog
* Thu Apr 25 2019 Tomas Orsava <torsava@redhat.com> - 1.0.18-6
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Mon Jul 16 2018 Lumír Balhar <lbalhar@redhat.com> - 1.0.18-5
- First version for python27 module
