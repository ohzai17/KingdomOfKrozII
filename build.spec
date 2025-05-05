import sys
import os

project_root = os.getcwd() # Get current working directory

src_path = os.path.join(project_root, 'src')
assets_dir_src = os.path.join(src_path, 'assets') # Path to assets in your source tree
assets_dir = 'src/assets' # Destination path INSIDE the bundle relative to the main script

# Icon paths relative to the spec file (project root)
icon_path_mac = os.path.join(src_path, 'assets', 'gameIcon.icns')
icon_path_win = os.path.join(src_path, 'assets', 'gameIcon.ico')


# --- Analysis Phase ---
# Tells PyInstaller where to find your code and what needs to be included.
a = Analysis(
    ['src/main.py'],                     # Your main script
    pathex=[project_root],               # Adds project root to Python path for imports
    binaries=[],                         # Any external binary files (usually empty)
    datas=[(assets_dir_src, assets_dir)], # IMPORTANT: Include your assets folder
    hiddenimports=[],                    # List modules PyInstaller might miss
    hookspath=[],                        # Paths to custom PyInstaller hooks
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)

# --- PYZ Archive ---
# Bundles pure Python modules.
pyz = PYZ(a.pure, a.zipped_data, cipher=None)


# --- macOS Configuration ---
if sys.platform == 'darwin':
    # --- Executable (Defined first for BUNDLE reference) ---
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name='KingdomOfKrozII',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None
    )
    # --- App Bundle (macOS) ---
    app = BUNDLE(
        exe, # Include the exe defined above
        name='KingdomOfKrozII.app',
        icon=icon_path_mac,
        bundle_identifier='com.yourdomain.kingdomofkroz2',
        info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSAppleScriptEnabled': False,
            'CFBundleShortVersionString':'1.0',
            'NSHighResolutionCapable': 'True',
            'NSSupportsAutomaticGraphicsSwitching': True,
            'LSMinimumSystemVersion': '11.0'
         }
    )

# --- Windows Configuration ---
elif sys.platform == 'win32':
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='KingdomOfKrozII',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=icon_path_win
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='KingdomOfKrozII'
    )

# --- Linux Configuration ---
elif sys.platform.startswith('linux'):
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='KingdomOfKrozII',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='KingdomOfKrozII'
    )