Summary:	Useful Vim editor buffer, file and window related functions
Summary(pl):	Przydatne funkcje dla Vima zwi±zane z buforami, plikami i oknami
Name:		vim-plugin-genutils
Version:	2.1
Release:	0.1
License:	GPL
Group:		Applications/Editors/Vim
Source0:	genutils-%{version}.zip
# Source0-md5:	25b93ab92cc8ca3bad9cb5fa3ddbfbb1
#URL:		fixme
Requires:	vim >= 4:6.3.058-3
Requires:	vim-plugin-multvals
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Useful Vim editor buffer, file and window related functions.

%description -l pl
Przydatne funkcje dla Vima zwi±zane z buforami, plikami i oknami.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/plugin/*
