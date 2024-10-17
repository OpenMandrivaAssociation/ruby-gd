%define name	ruby-gd
%define version	0.8.0
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    An interface to Boutell GD library
Group:      Development/Ruby
License:    BSD-like
URL:        https://rubyforge.org/projects/ruby-gd/
Source:     http://rubyforge.org/frs/download.php/39577/%{name}-%{version}.gem
BuildRequires:  gd-devel
BuildRequires:  ruby-devel
BuildRequires:  freetype2-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Ruby/GD (formerly known as "GD") is an extension
library to use Thomas Boutell's gd library
(http://www.boutell.com/gd/) from Ruby.

%prep
%setup -c
tar xzf data.tar.gz

%build
ruby extconf.rb --with-jpeg --with-freetype --with-ttf --enable-gd2_0

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{ruby_sitearchdir}/GD.so

