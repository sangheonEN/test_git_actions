# -*- mode: python ; coding: utf-8 -*-

# Add torch-specific collected data to the main analysis
a = Analysis(
    ['app/main.py'],
    pathex=[],
    binaries=[],  # Add torch binaries
    datas=[],  # Add torch datas
    hiddenimports=[],  # Add torch hidden imports
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='RealTimeSTT_Button_Mode',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=''
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='RealTimeSTT_Button_Mode',
)
