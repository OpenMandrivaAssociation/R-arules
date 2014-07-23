%bcond_without bootstrap
%global packname  arules
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.3
Release:          1
Summary:          Mining Association Rules and Frequent Itemsets
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/arules_1.1-3.tar.gz
Requires:         R-stats
Requires:         R-methods
Requires:         R-Matrix
%if %{without bootstrap}
Requires:         R-pmml
Requires:         R-arulesViz
%endif
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex
BuildRequires:    R-stats
BuildRequires:    R-methods
BuildRequires:    R-Matrix
%if %{without bootstrap}
BuildRequires:    R-pmml
BuildRequires:    R-arulesViz
%endif
BuildRequires:    pkgconfig(lapack)

%description
Provides the infrastructure for representing, manipulating and analyzing
transaction data and patterns (frequent itemsets and association rules).
Also provides interfaces to C implementations of the association mining
algorithms Apriori and Eclat by C. Borgelt.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
# %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
