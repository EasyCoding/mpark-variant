# This is a header-only library, but it install also cmake
# scripts to %%{_libdir}, so it cannot be noarch.
%global debug_package %{nil}

Name: mpark-variant
Summary: C++17 std::variant for C++11/14/17
Version: 1.3.0
Release: 1%{?dist}

License: Boost
URL: https://github.com/mpark/variant
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n variant-%{version} -p1
mkdir -p %{_target_platform}
sed -i 's@lib/@%{_libdir}/@g' CMakeLists.txt

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%files devel
%doc README.md
%license LICENSE.md
%{_includedir}/mpark
%{_libdir}/cmake/mpark_variant

%changelog
* Wed Jul 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3.0-1
- Initial SPEC release.
