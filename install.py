import os

os.system("pyinstaller -n MERK --onefile src/app.py")

# Todo: Switch to pyinstaller class
# import PyInstaller.__main__

# PyInstaller.__main__.run([
#     '--name=%s' % package_name,
#     '--onefile',
#     '--windowed',
#     '--add-binary=%s' % os.path.join('resource', 'path', '*.png'),
#     '--add-data=%s' % os.path.join('resource', 'path', '*.txt'),
#     '--icon=%s' % os.path.join('resource', 'path', 'icon.ico'),
#     os.path.join('my_package', '__main__.py'),
# ])