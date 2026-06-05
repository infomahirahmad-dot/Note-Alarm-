# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for Note Alarm
# Run: pyinstaller NoteAlarm.spec

import os
import sys

block_cipher = None

# Collect webview data files (DLLs etc.)
from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs
webview_data = collect_data_files('webview')
webview_bins = collect_dynamic_libs('webview')

a = Analysis(
    ['app.py'],
    pathex=['.'],
    binaries=webview_bins,
    datas=webview_data + [
        ('icon.ico', '.'),   # include icon if present
    ],
    hiddenimports=[
        'webview',
        'webview.platforms.winforms',
        'clr',
        'System',
        'System.Windows.Forms',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='NoteAlarm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # No console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',        # App icon
    version='version_info.txt',
)
