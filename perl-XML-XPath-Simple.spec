#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	XPath-Simple
Summary:	XML::XPath::Simple - very simple interface for XPaths
Summary(pl):	XML::XPath::Simple - bardzo prosty interfejs do XPath
Name:		perl-XML-XPath-Simple
Version:	0.05
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c97b04ecd031e7a27e5b8eb09a44928f
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.18
BuildRequires:	perl-XML-Simple >= 1.08
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl
XML::XPath::Simple zosta³ zaprojektowany aby umo¿liwiæ u¿ycie prostej
sk³adni Abbreviated XPath do dostêpu do warto¶ci z ma³ego dokumentu
XML. Ten modu³ nie ma byæ pe³nym zamiennikiem XML::XPath i nie
obs³uguje ca³ej rekomendacji XPath z W3C. Ma byæ prostym sposobem na
dostêp do danych XML z ma³ych, nie z³o¿onych struktur.

XML::XPath::Simple nie obs³uguje dokumentów z elementami o mieszanej
tre¶ci (tekst i znaczniki), nie pozwala te¿ na przemieszczanie po
strukturze drzewa ani liczenie elementów. O ile ten modu³ pozwala na
dostêp do okre¶lonych wêz³ów przy u¿yciu funkcji position(),
wewnêtrznie niekoniecznie analizuje strukturê XML-a w okre¶lonej
kolejno¶ci, wiêc wywo³ania position() mog± nie zwróciæ takiej
warto¶ci, jak± oczekiwano.

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
