from cx_Freeze import setup, Executable
import mysqlx.protobuf.mysqlx_notice_pb2
import google
import func

executables = [Executable('app.py', targetName='qt_app.exe')]

#excludes = ['logging', 'unittest', 'email', 'html', 'http', 'xml',
 #           'unicodedata', 'bz2', 'select']
excludes=[]

#zip_include_packages = ['collections', 'encodings', 'importlib', 'wx']
additional_mods=['mysqlx','func']


options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        #'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
        'includes':additional_mods
    }
}

setup(name='garage',
      version='0.0.1',
      description='garage odbc',
      executables=executables,
      options=options)
