#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : volk
Version  : 1.4
Release  : 1
URL      : https://github.com/gnuradio/volk/archive/v1.4.tar.gz
Source0  : https://github.com/gnuradio/volk/archive/v1.4.tar.gz
Summary  : VOLK: Vector Optimized Library of Kernels
Group    : Development/Tools
License  : GPL-3.0
Requires: volk-bin = %{version}-%{release}
Requires: volk-lib = %{version}-%{release}
Requires: volk-license = %{version}-%{release}
Requires: volk-python = %{version}-%{release}
Requires: volk-python3 = %{version}-%{release}
BuildRequires : Mako
BuildRequires : Mako-python3
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : git
BuildRequires : pkg-config
BuildRequires : python3
BuildRequires : six
BuildRequires : six-python3

%description
The volk_modtool tool is installed along with VOLK as a way of helping
to construct, add to, and interogate the VOLK library or companion
libraries.

%package bin
Summary: bin components for the volk package.
Group: Binaries
Requires: volk-license = %{version}-%{release}

%description bin
bin components for the volk package.


%package dev
Summary: dev components for the volk package.
Group: Development
Requires: volk-lib = %{version}-%{release}
Requires: volk-bin = %{version}-%{release}
Provides: volk-devel = %{version}-%{release}
Requires: volk = %{version}-%{release}

%description dev
dev components for the volk package.


%package lib
Summary: lib components for the volk package.
Group: Libraries
Requires: volk-license = %{version}-%{release}

%description lib
lib components for the volk package.


%package license
Summary: license components for the volk package.
Group: Default

%description license
license components for the volk package.


%package python
Summary: python components for the volk package.
Group: Default
Requires: volk-python3 = %{version}-%{release}

%description python
python components for the volk package.


%package python3
Summary: python3 components for the volk package.
Group: Default
Requires: python3-core

%description python3
python3 components for the volk package.


%prep
%setup -q -n volk-1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556836761
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1556836761
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/volk
cp COPYING %{buildroot}/usr/share/package-licenses/volk/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/volk-config-info
/usr/bin/volk_modtool
/usr/bin/volk_profile

%files dev
%defattr(-,root,root,-)
/usr/include/volk/saturation_arithmetic.h
/usr/include/volk/volk.h
/usr/include/volk/volk_16i_32fc_dot_prod_32fc.h
/usr/include/volk/volk_16i_branch_4_state_8.h
/usr/include/volk/volk_16i_convert_8i.h
/usr/include/volk/volk_16i_max_star_16i.h
/usr/include/volk/volk_16i_max_star_horizontal_16i.h
/usr/include/volk/volk_16i_permute_and_scalar_add.h
/usr/include/volk/volk_16i_s32f_convert_32f.h
/usr/include/volk/volk_16i_x4_quad_max_star_16i.h
/usr/include/volk/volk_16i_x5_add_quad_16i_x4.h
/usr/include/volk/volk_16ic_convert_32fc.h
/usr/include/volk/volk_16ic_deinterleave_16i_x2.h
/usr/include/volk/volk_16ic_deinterleave_real_16i.h
/usr/include/volk/volk_16ic_deinterleave_real_8i.h
/usr/include/volk/volk_16ic_magnitude_16i.h
/usr/include/volk/volk_16ic_s32f_deinterleave_32f_x2.h
/usr/include/volk/volk_16ic_s32f_deinterleave_real_32f.h
/usr/include/volk/volk_16ic_s32f_magnitude_32f.h
/usr/include/volk/volk_16ic_x2_dot_prod_16ic.h
/usr/include/volk/volk_16ic_x2_multiply_16ic.h
/usr/include/volk/volk_16u_byteswap.h
/usr/include/volk/volk_16u_byteswappuppet_16u.h
/usr/include/volk/volk_32f_64f_add_64f.h
/usr/include/volk/volk_32f_64f_multiply_64f.h
/usr/include/volk/volk_32f_8u_polarbutterfly_32f.h
/usr/include/volk/volk_32f_8u_polarbutterflypuppet_32f.h
/usr/include/volk/volk_32f_accumulator_s32f.h
/usr/include/volk/volk_32f_acos_32f.h
/usr/include/volk/volk_32f_asin_32f.h
/usr/include/volk/volk_32f_atan_32f.h
/usr/include/volk/volk_32f_binary_slicer_32i.h
/usr/include/volk/volk_32f_binary_slicer_8i.h
/usr/include/volk/volk_32f_convert_64f.h
/usr/include/volk/volk_32f_cos_32f.h
/usr/include/volk/volk_32f_expfast_32f.h
/usr/include/volk/volk_32f_index_max_16u.h
/usr/include/volk/volk_32f_index_max_32u.h
/usr/include/volk/volk_32f_invsqrt_32f.h
/usr/include/volk/volk_32f_log2_32f.h
/usr/include/volk/volk_32f_null_32f.h
/usr/include/volk/volk_32f_s32f_32f_fm_detect_32f.h
/usr/include/volk/volk_32f_s32f_calc_spectral_noise_floor_32f.h
/usr/include/volk/volk_32f_s32f_convert_16i.h
/usr/include/volk/volk_32f_s32f_convert_32i.h
/usr/include/volk/volk_32f_s32f_convert_8i.h
/usr/include/volk/volk_32f_s32f_mod_rangepuppet_32f.h
/usr/include/volk/volk_32f_s32f_multiply_32f.h
/usr/include/volk/volk_32f_s32f_normalize.h
/usr/include/volk/volk_32f_s32f_power_32f.h
/usr/include/volk/volk_32f_s32f_s32f_mod_range_32f.h
/usr/include/volk/volk_32f_s32f_stddev_32f.h
/usr/include/volk/volk_32f_sin_32f.h
/usr/include/volk/volk_32f_sqrt_32f.h
/usr/include/volk/volk_32f_stddev_and_mean_32f_x2.h
/usr/include/volk/volk_32f_tan_32f.h
/usr/include/volk/volk_32f_tanh_32f.h
/usr/include/volk/volk_32f_x2_add_32f.h
/usr/include/volk/volk_32f_x2_divide_32f.h
/usr/include/volk/volk_32f_x2_dot_prod_16i.h
/usr/include/volk/volk_32f_x2_dot_prod_32f.h
/usr/include/volk/volk_32f_x2_fm_detectpuppet_32f.h
/usr/include/volk/volk_32f_x2_interleave_32fc.h
/usr/include/volk/volk_32f_x2_max_32f.h
/usr/include/volk/volk_32f_x2_min_32f.h
/usr/include/volk/volk_32f_x2_multiply_32f.h
/usr/include/volk/volk_32f_x2_pow_32f.h
/usr/include/volk/volk_32f_x2_s32f_interleave_16ic.h
/usr/include/volk/volk_32f_x2_subtract_32f.h
/usr/include/volk/volk_32f_x3_sum_of_poly_32f.h
/usr/include/volk/volk_32fc_32f_add_32fc.h
/usr/include/volk/volk_32fc_32f_dot_prod_32fc.h
/usr/include/volk/volk_32fc_32f_multiply_32fc.h
/usr/include/volk/volk_32fc_conjugate_32fc.h
/usr/include/volk/volk_32fc_convert_16ic.h
/usr/include/volk/volk_32fc_deinterleave_32f_x2.h
/usr/include/volk/volk_32fc_deinterleave_64f_x2.h
/usr/include/volk/volk_32fc_deinterleave_imag_32f.h
/usr/include/volk/volk_32fc_deinterleave_real_32f.h
/usr/include/volk/volk_32fc_deinterleave_real_64f.h
/usr/include/volk/volk_32fc_index_max_16u.h
/usr/include/volk/volk_32fc_index_max_32u.h
/usr/include/volk/volk_32fc_magnitude_32f.h
/usr/include/volk/volk_32fc_magnitude_squared_32f.h
/usr/include/volk/volk_32fc_s32f_atan2_32f.h
/usr/include/volk/volk_32fc_s32f_deinterleave_real_16i.h
/usr/include/volk/volk_32fc_s32f_magnitude_16i.h
/usr/include/volk/volk_32fc_s32f_power_32fc.h
/usr/include/volk/volk_32fc_s32f_power_spectrum_32f.h
/usr/include/volk/volk_32fc_s32f_x2_power_spectral_density_32f.h
/usr/include/volk/volk_32fc_s32fc_multiply_32fc.h
/usr/include/volk/volk_32fc_s32fc_rotatorpuppet_32fc.h
/usr/include/volk/volk_32fc_s32fc_x2_rotator_32fc.h
/usr/include/volk/volk_32fc_x2_add_32fc.h
/usr/include/volk/volk_32fc_x2_conjugate_dot_prod_32fc.h
/usr/include/volk/volk_32fc_x2_divide_32fc.h
/usr/include/volk/volk_32fc_x2_dot_prod_32fc.h
/usr/include/volk/volk_32fc_x2_multiply_32fc.h
/usr/include/volk/volk_32fc_x2_multiply_conjugate_32fc.h
/usr/include/volk/volk_32fc_x2_s32f_square_dist_scalar_mult_32f.h
/usr/include/volk/volk_32fc_x2_square_dist_32f.h
/usr/include/volk/volk_32i_s32f_convert_32f.h
/usr/include/volk/volk_32i_x2_and_32i.h
/usr/include/volk/volk_32i_x2_or_32i.h
/usr/include/volk/volk_32u_byteswap.h
/usr/include/volk/volk_32u_byteswappuppet_32u.h
/usr/include/volk/volk_32u_popcnt.h
/usr/include/volk/volk_32u_popcntpuppet_32u.h
/usr/include/volk/volk_32u_reverse_32u.h
/usr/include/volk/volk_64f_convert_32f.h
/usr/include/volk/volk_64f_x2_add_64f.h
/usr/include/volk/volk_64f_x2_max_64f.h
/usr/include/volk/volk_64f_x2_min_64f.h
/usr/include/volk/volk_64f_x2_multiply_64f.h
/usr/include/volk/volk_64u_byteswap.h
/usr/include/volk/volk_64u_byteswappuppet_64u.h
/usr/include/volk/volk_64u_popcnt.h
/usr/include/volk/volk_64u_popcntpuppet_64u.h
/usr/include/volk/volk_8i_convert_16i.h
/usr/include/volk/volk_8i_s32f_convert_32f.h
/usr/include/volk/volk_8ic_deinterleave_16i_x2.h
/usr/include/volk/volk_8ic_deinterleave_real_16i.h
/usr/include/volk/volk_8ic_deinterleave_real_8i.h
/usr/include/volk/volk_8ic_s32f_deinterleave_32f_x2.h
/usr/include/volk/volk_8ic_s32f_deinterleave_real_32f.h
/usr/include/volk/volk_8ic_x2_multiply_conjugate_16ic.h
/usr/include/volk/volk_8ic_x2_s32f_multiply_conjugate_32fc.h
/usr/include/volk/volk_8u_conv_k7_r2puppet_8u.h
/usr/include/volk/volk_8u_x2_encodeframepolar_8u.h
/usr/include/volk/volk_8u_x3_encodepolar_8u_x2.h
/usr/include/volk/volk_8u_x3_encodepolarpuppet_8u.h
/usr/include/volk/volk_8u_x4_conv_k7_r2_8u.h
/usr/include/volk/volk_avx_intrinsics.h
/usr/include/volk/volk_common.h
/usr/include/volk/volk_complex.h
/usr/include/volk/volk_config_fixed.h
/usr/include/volk/volk_cpu.h
/usr/include/volk/volk_malloc.h
/usr/include/volk/volk_neon_intrinsics.h
/usr/include/volk/volk_prefs.h
/usr/include/volk/volk_sse3_intrinsics.h
/usr/include/volk/volk_sse_intrinsics.h
/usr/include/volk/volk_typedefs.h
/usr/lib64/cmake/volk/VolkConfig.cmake
/usr/lib64/cmake/volk/VolkConfigVersion.cmake
/usr/lib64/libvolk.so
/usr/lib64/pkgconfig/volk.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvolk.so.1.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/volk/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*