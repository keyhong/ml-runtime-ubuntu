# pandoc-installtion

```bash
$ export COMMON_PKG_HOME=/home/cdsw/packages/ubuntu_packages/home

$ apt-get reinstall -y --no-install-recommends --download-only \
    pandoc \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic

$ find /var/cache/apt/archives/ -maxdepth 1 -name "*.deb" -mmin -1 -exec mv -t /home/cdsw/packages/ubuntu_packages/common/pandoc {} +


```