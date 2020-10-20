import os
import sys
import shutil
import PyInstaller.__main__

package_name = 'MERK'

def install():
    PyInstaller.__main__.run([
        '--log-level=INFO',
        '--name=%s' % package_name,
        '--onefile',
        '--clean',
        '--icon=%s' % os.path.join('resources', 'icon.ico'),
        os.path.join('src', 'app.py'),
    ])

def del_folder(folder_name: str):
    dir_path = (os.path.join(os.path.abspath(os.getcwd()),folder_name))
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
        print(f"{folder_name} folder either does not exist, or cannot be modified")

if 'clean' in sys.argv:
    print('Cleaning existing installation\n')
    del_folder('build')
    del_folder('dist')
    print('/build and /dist directories removed')
else:
    print('INSTALLING...\n')
    install()
    print('Installation complete')

# os.system("pyinstaller -n MERK --onefile src/app.py")