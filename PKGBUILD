# Maintainer: saeed badreldin <helwanlinux@gmail.com>
pkgname=hel-cmd-runner
pkgver=0.0.1
pkgrel=2
pkgdesc="A terminal-style runner game to learn Helwan Linux commands"
arch=('any')
url="https://github.com/helwan-linux/hel-cmd-runner"
license=('GPL')
depends=('python' 'python-pygame')
makedepends=('git')
source=("git+${url}.git")
md5sums=('SKIP')

package() {
    # 1. إعداد المجلدات 
    install -d "${pkgdir}/opt/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/applications"
    install -d "${pkgdir}/usr/share/pixmaps"

    # 2. الدخول لمجلد المشروع داخل المستودع 
    cd "${srcdir}/hel-cmd-runner/hel-cmd"

    # 3. نسخ ملفات اللعبة إلى /opt/ 
    cp -r engine logic ui images data main.py "${pkgdir}/opt/${pkgname}/"

    # 4. إنشاء ملف تشغيل (Wrapper) لضمان العمل من المسار الصحيح [cite: 3, 4]
    # تم تعديل الأمر لضمان استدعاء python3 واستخدام متغير الـ pkgname
    echo -e "#!/bin/bash\ncd /opt/${pkgname} && python3 main.py \"\$@\"" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"

    # 5. تعديل ملف الـ .desktop برمجياً ليتناسب مع مسارات النظام الجديد 
    # بنستخدم sed عشان نضمن إن الـ Exec بيشاور على الـ wrapper اللي عملناه
    sed -i 's|Exec=.*|Exec=hel-cmd-runner|' helwan-runner.desktop
    sed -i 's|Icon=.*|Icon=helwan-runner|' helwan-runner.desktop
    
    # 6. تثبيت ملف اللانشر والأيقونة 
    install -m 644 "helwan-runner.desktop" "${pkgdir}/usr/share/applications/"
    install -m 644 "images/icon.png" "${pkgdir}/usr/share/pixmaps/helwan-runner.png"

    # 7. ضبط صلاحيات مجلد البيانات للـ Highscores 
    chmod -R 777 "${pkgdir}/opt/${pkgname}/data"
}
