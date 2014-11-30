#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	XPath-Simple
%include	/usr/lib/rpm/macros.perl
Summary:	XML::XPath::Simple - very simple interface for XPaths
Summary(pl.UTF-8):	XML::XPath::Simple - bardzo prosty interfejs do XPath
Name:		perl-XML-XPath-Simple
Version:	0.05
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c97b04ecd031e7a27e5b8eb09a44928f
URL:		http://search.cpan.org/dist/XML-XPath-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.18
BuildRequires:	perl-XML-Simple >= 1.08
%endif
Requires:	perl-XML-Simple >= 1.08
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::XPath::Simple is designed to allow for the use of simple
Abbreviated XPath syntax to access values from a small XML document.
This module is not meant as a drop-in replacement for XML::XPath, and
doesn't support the entire W3C XPath Recommendation. This module is
meant as an easy and simple way to access XML data from small,
non-complex structures.

XML::XPath::Simple doesn't support documents that have elements
containing mixed content (text and tags), nor does it allow for the
walking of the tree structure, or the counting of elements. While this
module allows access to specific nodes using the position() function,
internally the module doesn't necessarially parse the XML structure in
any specific order, so position() calls may not return the value
expected.

%description -l pl.UTF-8
XML::XPath::Simple został zaprojektowany aby umożliwić użycie prostej
składni Abbreviated XPath do dostępu do wartości z małego dokumentu
XML. Ten moduł nie ma być pełnym zamiennikiem XML::XPath i nie
obsługuje całej rekomendacji XPath z W3C. Ma być prostym sposobem na
dostęp do danych XML z małych, nie złożonych struktur.

XML::XPath::Simple nie obsługuje dokumentów z elementami o mieszanej
treści (tekst i znaczniki), nie pozwala też na przemieszczanie po
strukturze drzewa ani liczenie elementów. O ile ten moduł pozwala na
dostęp do określonych węzłów przy użyciu funkcji position(),
wewnętrznie niekoniecznie analizuje strukturę XML-a w określonej
kolejności, więc wywołania position() mogą nie zwrócić takiej
wartości, jaką oczekiwano.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/XPath/Simple.pm
%{_mandir}/man3/*
