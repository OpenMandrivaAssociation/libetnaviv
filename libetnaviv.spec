%define major	1
%define libname	%mklibname fakedrm_etnaviv %{major}
%define devname	%mklibname -d fakedrm_etnaviv
%define snap	20191215

Summary:	This library completely wraps the kernel interface
Name:		libetnaviv
Version:	0.0.0
Release:	0.%{snap}.1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/etnaviv/libetnaviv
Source0:	https://github.com/etnaviv/libetnaviv/archive/imx8.tar.gz
Source1:	https://github.com/etnaviv/galcore_headers/archive/master.tar.gz

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
%autosetup -n %{name}-imx8 -a 1
autoreconf -fiv

%build
%configure \
	--with-galcore-include="$(pwd)"/galcore_headers-master/include_imx8_v6.2.3.129602 \
	--disable-static \

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libfakedrm_etnaviv.so.%{major}*

%files -n %{devname}
%{_libdir}/libfakedrm_etnaviv.so
%{_includedir}/etnaviv
%{_libdir}/pkgconfig/*.pc
