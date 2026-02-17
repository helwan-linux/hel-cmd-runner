# Maintainer: saeed badreldin helwanlinux@gmail.com
pkgname=hel-cmd-runner
pkgver=1.0.0
pkgrel=1
pkgdesc="A terminal-style runner game to learn Helwan Linux commands"
arch=('any')
url="https://github.com/helwan-linux/hel-cmd-runner"
license=('GPL')
depends=('python' 'python-pygame')
makedepends=('git')
source=("git+${url}.git")
md5sums=('SKIP')

package() {
    # 1. Create system directories
    install -d "${pkgdir}/opt/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/applications"
    install -d "${pkgdir}/usr/share/pixmaps"

    # 2. Copy the whole source to /opt/ (Cleaner than /usr/share/)
    cd "${srcdir}/${pkgname}"
    cp -r engine logic ui images data main.py "${pkgdir}/opt/${pkgname}/"

    # 3. Create the executable binary in /usr/bin
    echo -e "#!/bin/bash\ncd /opt/${pkgname} && python main.py \"\$@\"" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"

    # 4. Install Desktop entry and Icon
    # Note: Ensure the .desktop file in your repo has Icon=helwan-runner
    install -m 644 "helwan-runner.desktop" "${pkgdir}/usr/share/applications/"
    install -m 644 "images/icon.png" "${pkgdir}/usr/share/pixmaps/helwan-runner.png"

    # 5. Correct permissions for data files
    chmod -R 777 "${pkgdir}/opt/${pkgname}/data"
}
