# Maintainer: saeed badreldin <helwanlinux@gmail.com>
pkgname=hel-cmd-runner
pkgver=0.0.1
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
    # 1. Directories setup
    install -d "${pkgdir}/opt/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/applications"
    install -d "${pkgdir}/usr/share/pixmaps"

    # 2. Go into the project folder inside the cloned repo
    cd "${srcdir}/hel-cmd-runner/hel-cmd"

    # 3. Deploy game files to /opt/
    cp -r engine logic ui images data main.py "${pkgdir}/opt/${pkgname}/"

    # 4. Create the system binary
    echo -e "#!/bin/bash\ncd /opt/${pkgname} && python main.py \"\$@\"" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"

    # 5. Install Desktop entry and Icon
    install -m 644 "helwan-runner.desktop" "${pkgdir}/usr/share/applications/"
    install -m 644 "images/icon.png" "${pkgdir}/usr/share/pixmaps/helwan-runner.png"

    # 6. Set data directory permissions
    chmod -R 777 "${pkgdir}/opt/${pkgname}/data"
}
