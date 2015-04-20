%define major	1
%define libname	%mklibname etnaviv %{major}
%define devname	%mklibname -d etnaviv
%define snap	20150420

Summary:	This library completely wraps the kernel interface
Name:		libetnaviv
Version:	0.0.0
Release:	0.%{snap}.1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/etnaviv/libetnaviv
Source0:	%{name}-%{version}-%{snap}.tar.xz
Source1:	headers-HAL-0.0.0-%{snap}.tar.xz

%description
Library for:
a) ioctl (kernel interface) wrapping
b) video memory management
c) command buffer and event queue handling
d) context / state delta handling (still incomplete)
e) register description headers
f) converting surfaces and textures from and to Vivante specific tiling formats

%package -n	%{libname}
Summary:	Library for accessing USB devices
Group:		System/Libraries

%description -n	%{libname}
Library for:
a) ioctl (kernel interface) wrapping
b) video memory management
c) command buffer and event queue handling
d) context / state delta handling (still incomplete)
e) register description headers
f) converting surfaces and textures from and to Vivante specific tiling formats

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -qn %{name}-%{version}-%{snap}
tar -xvf %{SOURCE1}
autoreconf -fiv

%build
%configure \
	--with-galcore-include="$(pwd)"/headers-HAL-0.0.0-%{snap} \
	--disable-static \

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libetnaviv.so.%{major}*

%files -n %{devname}
%{_libdir}/libetnaviv.so
%{_includedir}/etnaviv/*.h
%{_libdir}/pkgconfig/libetnaviv.pc
