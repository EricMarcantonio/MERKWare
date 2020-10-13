import os
import PyInstaller.__main__

package_name = 'MERK'

PyInstaller.__main__.run([
    '--log-level=DEBUG',
    '--name=%s' % package_name,
    '--onefile',
    '--clean',
    '--icon=%s' % os.path.join('resources', 'icon.ico'),
    os.path.join('src', 'app.py'),
])

# os.system("pyinstaller -n MERK --onefile src/app.py")