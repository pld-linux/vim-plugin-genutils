Summary:	Useful Vim editor buffer, file and window related functions
Summary(pl.UTF-8):   Przydatne funkcje dla Vima związane z buforami, plikami i oknami
Name:		vim-plugin-genutils
Version:	2.3
Release:	1
License:	GPL
Group:		Applications/Editors/Vim
Source0:	genutils-%{version}.zip
# Source0-md5:	4a633cb703cdd596203063c31969f59e
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=197
Requires:	vim >= 4:7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Useful Vim editor buffer, file and window related functions.

%description -l pl.UTF-8
Przydatne funkcje dla Vima związane z buforami, plikami i oknami.

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
