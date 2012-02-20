%bcond_without bootstrap
%global packname  arules
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0_7
Release:          1
Summary:          Mining Association Rules and Frequent Itemsets
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-7.tar.gz
Requires:         R-stats R-methods R-Matrix 
%if %{without bootstrap}
Requires:         R-pmml R-arulesViz 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-methods R-Matrix
%if %{without bootstrap}
BuildRequires:    R-pmml R-arulesViz 
%endif

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
