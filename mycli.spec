# -*- mode: python -*-
a = Analysis(['mycli.py'],
             pathex=['/home/kamal/python/test-pyinstaller/vendor', '/home/kamal/python/test-pyinstaller'],
             hiddenimports=['baker'],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mycli',
          debug=False,
          strip=None,
          upx=True,
          console=True )
