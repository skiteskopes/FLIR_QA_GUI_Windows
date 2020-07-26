# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['qa_gui.py'],
             pathex=['C:\\Users\\Gaming Pc\\Desktop\\FLIR_QA_GUI'],
             binaries=[],
             datas=[],
             hiddenimports=['imagecodecs._imagecodecs_lite'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='qa_gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='flir.ico')
