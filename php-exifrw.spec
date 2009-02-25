# TODO
# - hardcoded cacheDir
Summary:	An EXIF information reader and write PHP classes
Name:		php-exifrw
Version:	1.1
Release:	1
License:	LGPL v2+
Group:		Development/Languages/PHP
URL:		http://www.vinayras.com/project/phpexifrw.php
Source0:	http://www.vinayras.com/projects/phpExifRW-%{version}.tar.gz
# Source0-md5:	27a9313e8682e54db9f2255ffac7de60
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class to parse out JPEG files and extract EXIF infromation that most
digital camera produces. Exif information can also be transfered from
one file to another. Thumbnail is also extracted.

%prep
%setup -q -n phpExifRW-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{_examplesdir}/%{name}-%{version}}
cp -a showThumbnail.php exampleReader.php exampleWriter.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a exifReader.inc exifWriter.inc $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES readme.txt
%{php_data_dir}/exifReader.inc
%{php_data_dir}/exifWriter.inc
%{_examplesdir}/%{name}-%{version}
