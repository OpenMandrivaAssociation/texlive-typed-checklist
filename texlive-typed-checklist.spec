Name:		texlive-typed-checklist
Version:	63445
Release:	2
Summary:	Typesetting tasks, goals, milestones, artifacts, and more in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/typed-checklist
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typed-checklist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typed-checklist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typed-checklist.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The main goal of this package is to provide means for
typesetting checklists in a way that stipulates users to
explicitly distinguish checklists for goals, for tasks, for
artifacts, and for milestones -- i.e., the type of checklist
entries. The intention behind this is that a user of the
package is coerced to think about what kind of entries he/she
adds to the checklist. This shall yield a clearer result and,
in the long run, help with training to distinguish entries of
different types.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/typed-checklist
%{_texmfdistdir}/tex/latex/typed-checklist
%doc %{_texmfdistdir}/doc/latex/typed-checklist

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
