%include	/usr/lib/rpm/macros.perl
Summary:	CLOC - Count Lines of Code
Name:		cloc
Version:	1.84
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/AlDanial/cloc/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a52f3843825377cfa4e4b3b30a567ab4
URL:		https://github.com/AlDanial/cloc
BuildRequires:	perl-Regexp-Common
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cloc counts blank lines, comment lines, and physical lines of source
code in many programming languages. Given two versions of a code base,
cloc can also compute differences in blank, comment, and source lines.

%prep
%setup -q

# fix #!env perl -w -> #!%{__perl}:
%{__sed} -e '1s,^#!.*perl,#!%{__perl},' Unix/cloc

%build
%{__make} -C Unix

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C Unix install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md sqlite_formatter
%doc Unix/{AUTHORS,COPYING,INSTALL,NEWS,README}
%attr(755,root,root) %{_bindir}/cloc
%{_mandir}/man1/cloc.1*
