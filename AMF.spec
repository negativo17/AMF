Name:           AMF
Version:        1.4.23
Release:        1%{?dist}
Summary:        Advanced Media Framework (AMF) SDK
License:        MIT
URL:            https://gpuopen.com/advanced-media-framework/
BuildArch:      noarch

Source0:        https://github.com/GPUOpen-LibrariesAndSDKs/AMF/archive/v%{version}/%{name}-%{version}.tar.gz

#BuildRequires:  
#Requires:       

%description
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

%package        devel
Summary:        Development files for %{name}

%description    devel
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample files for %{name}

%description    samples
The %{name}-samples package contains sample programs and source for applications
that use %{name}.

%prep
%autosetup -p1

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -fr amf/public/include/* %{buildroot}%{_includedir}/%{name}/

mkdir -p %{buildroot}%{_usrsrc}/%{name}
cp -fr amf/public/* %{buildroot}%{_usrsrc}/%{name}/
rm -fr %{buildroot}%{_usrsrc}/%{name}/include
ln -sf ../../include/AMF %{buildroot}%{_usrsrc}/%{name}/include

%files devel
%license LICENSE.txt
%doc amf/doc/*
%{_includedir}/%{name}/

%files samples
%doc amf/doc/*
%{_usrsrc}/%{name}

%changelog
* Thu Feb 10 2022 Simone Caronni <negativo17@gmail.com> - 1.4.23-1
- First build.
