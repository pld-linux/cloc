%include	/usr/lib/rpm/macros.perl
Summary:	CLOC - Count Lines of Code
Name:		cloc
Version:	1.55
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/cloc/%{name}-%{version}.pl
# Source0-md5:	19ab5852617e89d853793a693eb5e510
Source1:	http://downloads.sourceforge.net/cloc/release-%{version}.txt
# Source1-md5:	cb2e63726afc46faa68e1b144273dc0b
URL:		http://cloc.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cloc counts blank lines, comment lines, and physical lines of source
code in many programming languages. Given two versions of a code base,
cloc can also compute differences in blank, comment, and source lines.

%prep
%setup -qcT
cp -p %{SOURCE1} release.txt

# fix #!env perl -w -> #!%{__perl}:
%{__sed} -e '1s,^#!.*perl,#!%{__perl},' %{SOURCE0} > %{name}.pl
touch -r %{SOURCE0} %{name}.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name}.pl $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc release.txt
%attr(755,root,root) %{_bindir}/cloc
