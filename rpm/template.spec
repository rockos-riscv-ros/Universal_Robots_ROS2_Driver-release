%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-ur-robot-driver
Version:        3.0.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ur_robot_driver package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-backward-ros
Requires:       ros-jazzy-controller-manager
Requires:       ros-jazzy-controller-manager-msgs
Requires:       ros-jazzy-force-torque-sensor-broadcaster
Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-hardware-interface
Requires:       ros-jazzy-joint-state-broadcaster
Requires:       ros-jazzy-joint-state-publisher
Requires:       ros-jazzy-joint-trajectory-controller
Requires:       ros-jazzy-launch
Requires:       ros-jazzy-launch-ros
Requires:       ros-jazzy-pluginlib
Requires:       ros-jazzy-pose-broadcaster
Requires:       ros-jazzy-position-controllers
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-lifecycle
Requires:       ros-jazzy-rclpy
Requires:       ros-jazzy-robot-state-publisher
Requires:       ros-jazzy-ros2-controllers-test-nodes
Requires:       ros-jazzy-rviz2
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-std-srvs
Requires:       ros-jazzy-tf2-geometry-msgs
Requires:       ros-jazzy-ur-client-library
Requires:       ros-jazzy-ur-controllers
Requires:       ros-jazzy-ur-dashboard-msgs
Requires:       ros-jazzy-ur-description
Requires:       ros-jazzy-ur-msgs
Requires:       ros-jazzy-urdf
Requires:       ros-jazzy-velocity-controllers
Requires:       ros-jazzy-xacro
Requires:       socat
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-ament-cmake-python
BuildRequires:  ros-jazzy-backward-ros
BuildRequires:  ros-jazzy-controller-manager
BuildRequires:  ros-jazzy-controller-manager-msgs
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-hardware-interface
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-lifecycle
BuildRequires:  ros-jazzy-rclpy
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-std-srvs
BuildRequires:  ros-jazzy-tf2-geometry-msgs
BuildRequires:  ros-jazzy-ur-client-library
BuildRequires:  ros-jazzy-ur-controllers
BuildRequires:  ros-jazzy-ur-dashboard-msgs
BuildRequires:  ros-jazzy-ur-description
BuildRequires:  ros-jazzy-ur-msgs
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-launch-testing-ament-cmake
%endif

%description
The new driver for Universal Robots UR3, UR5 and UR10 robots with CB3
controllers and the e-series.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Thu Jan 23 2025 Felix Exner <feex@universal-robots.com> - 3.0.2-1
- Autogenerated by Bloom

* Thu Jan 02 2025 Felix Exner <feex@universal-robots.com> - 3.0.1-1
- Autogenerated by Bloom

* Wed Dec 18 2024 Felix Exner <feex@universal-robots.com> - 3.0.0-1
- Autogenerated by Bloom

* Tue Oct 29 2024 Felix Exner <exner@fzi.de> - 2.4.13-1
- Autogenerated by Bloom

* Mon Oct 14 2024 Felix Exner <exner@fzi.de> - 2.4.12-1
- Autogenerated by Bloom

* Thu Sep 12 2024 Felix Exner <exner@fzi.de> - 2.4.10-1
- Autogenerated by Bloom

* Sun Aug 11 2024 Denis Stogl <denis@stoglrobotics.de> - 2.4.9-1
- Autogenerated by Bloom

* Mon Jul 01 2024 Denis Stogl <denis@stoglrobotics.de> - 2.4.8-1
- Autogenerated by Bloom

* Sat May 18 2024 Denis Stogl <denis@stoglrobotics.de> - 2.4.5-1
- Autogenerated by Bloom

