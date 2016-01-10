Name:			nmon
Version:		16b
Release:		1%{?dist}
Summary:		Nigel's performance Monitor for Linux
License:		GPLv3
Group:			Development/Tools
URL:			http://nmon.sourceforge.net
Source:			http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
nmon is a systems administrator, tuner, benchmark tool, which provides 
information about CPU, disks, network, etc., all in one view.

%prep
%setup -q
sed -e "s/\r//" Documentation.txt > Documentation.txt
touch -c -r Documentation.txt Documentation.txt
ln -s lmon%{version}.c lmon.c

%build
make %{_smp_mflags}

%install
install -D -p -m 0755 %{name}_* %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc Documentation.txt 
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}

%changelog
* Sun Jan 10 2016 Andreas Guther <github@guther.net> - 16b-1
- Update to version 16b

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14i-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14i-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Palle Ravn <ravnzon@gmail.com> - 14i-6
- Update to version 14i
- GCC options modified for x86

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Palle Ravn <ravnzon@gmail.com> 14h-4
- Update to version 14h

* Mon Mar 18 2013 Palle Ravn <ravnzon@gmail.com> 14g-3
- Streamline download links
- Include manpage from sourceforges patch section
- No longer mark manpage as %%doc
- Only handle manpage in %%install

* Fri Mar 1 2013 Palle Ravn <ravnzon@gmail.com> 14g-2
- Add name macro to source links
- Add name macro to compile and install commands
- Add support for PowerPC compilation
- Remove redundant compile flags
- Changed to arbitrary manpage compression
- Preserve timestamps of Source1

* Mon Feb 25 2013 Palle Ravn <ravnzon@gmail.com> 14g-1
- Initial package
