# Maintainer: saeed badreldin <helwanlinux@gmail.com>
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

    # 2. Navigate to the project folder inside the repo
    # دخلنا للفولدر اللي فيه الكود فعلياً hel-cmd
    cd "${srcdir}/${pkgname}/hel-cmd"

    # 3. Copy only the necessary game files/folders
    cp -r engine logic ui images data main.py "${pkgdir}/opt/${pkgname}/"

    # 4. Create the executable binary in /usr/bin
    echo -e "#!/bin/bash\ncd /opt/${pkgname} && python main.py \"\$@\"" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"

    # 5. Install Desktop entry (it's in the repo root, so we go back one level)
    install -m 644 "${srcdir}/${pkgname}/helwan-runner.desktop" "${pkgdir}/usr/share/applications/"
    install -m 644 "images/icon.png" "${pkgdir}/usr/share/pixmaps/helwan-runner.png"

    # 6. Correct permissions for data files
    chmod -R 777 "${pkgdir}/opt/${pkgname}/data"
}
