Name:           libhybris-piglit
Version:        0.0.1
Release:        1
Summary:        Collection of automated tests for OpenGL/ES
Source0:        %{name}-%{version}.tar.gz
Patch0:         0001-Fix-build-and-run-issues-with-non-X11-Linux-platform.patch
Group:          Development/Tools
License:        BSD
URL:            http://people.freedesktop.org/~nh/piglit/

BuildRequires:  cmake
BuildRequires:  libEGL-devel
BuildRequires:  libwayland-egl-devel
BuildRequires:  libGLESv1-devel
BuildRequires:  libGLESv2-devel

BuildRequires:  python
BuildRequires:  python-mako
BuildRequires:  numpy
BuildRequires:  libhybris-waffle-devel
Requires:       python

%description
Piglit is a collection of automated tests for OpenGL and OpenCL
implementations. The goal of Piglit is to help improve the quality
of open source OpenGL and OpenCL drivers by providing developers
with a simple means to perform regression tests.

%prep
%setup -q
%patch0 -p1 -d piglit

%build
cd piglit
cmake -DCMAKE_INSTALL_PREFIX=/opt/tests/piglit \
      -DPIGLIT_BUILD_GL_TESTS=OFF \
      -DPIGLIT_BUILD_CL_TESTS=OFF \
      -DPIGLIT_BUILD_GLES1_TESTS=ON \
      -DPIGLIT_BUILD_GLES2_TESTS=ON \
      -DPIGLIT_BUILD_GLES3_TESTS=OFF \
      -DPIGLIT_BUILD_GLX_TESTS=OFF \
      -DPIGLIT_USE_WAFFLE=ON
make

%install
cd piglit
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
/opt/tests/piglit/*
