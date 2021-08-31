# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['ImageEditor.py', 'ImageEditor.spec'],
             pathex=['/Users/yuta-iida/Documents/ImageEditor'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['.'],
             hooksconfig={},
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
          [],
          exclude_binaries=True,
          name='ImageEditor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ImageEditor')
app = BUNDLE(coll,
             name='ImageEditor.app',
             icon='icon.icns',
             bundle_identifier=None,
             version='1.0.0',
             info_plist={
               'NSPrincipalClass': 'ImageEditor',
               'NSAppleScriptEnabled': False,
               'CFBundleDocumentTypes': [
                 {
                   'CFBundleTypeName': 'ImageEditor',
                   'CFBundleTypeIconFile': 'icon.icns',
                   'LSItemContentTypes': ['public.folder'],
                   'LSHandlerRank': 'Owner'
                 }
               ]
             },
           )
