%define		_snap	20060805
Summary:	ReportLab C accelerator extension
Summary(pl.UTF-8):	Rozszerzenie akceleratora C dla ReportLaba
Name:		rl_accel
Version:	0.58
Release:	0.%{_snap}.1
License:	GPL
Group:		Applications
Source0:	http://www.reportlab.org/daily/%{name}-%{version}-daily-unix.tgz
# Source0-md5:	7b0d606bc08caab63cf21b10a417ddda
URL:		http://www.reportlab.org/downloads.html#rl_accel
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ReportLab C accelerator extension, recommended for production use of
ReportLab.

%description -l pl.UTF-8
Rozszerzenie akceleratora C zalecane do produkcyjnego używania
ReportLaba.

%prep
%setup -q -n %{name}-%{version}-%{_snap}

%build
cd rl_accel
%{__python} ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
cd rl_accel
%{__python} ./setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
