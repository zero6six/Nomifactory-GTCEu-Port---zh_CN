import zipfile
import os
import shutil

# path of compressed file
zip_path = 'output//nomi-ceu-translations-zh_Hans.zip'
# temp folder for unzipping
temp_dir = 'output//temp_dir'
# output folder
target_root_dir = 'output//extracted_content'

# output names
target_subdirs = ['nomi-ceu', 'gregtech-drawers', 'nomi-labs']

# create folders
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
if not os.path.exists(target_root_dir):
    os.makedirs(target_root_dir)

# unzip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)

# iterate through temp folder
for root, dirs, files in os.walk(temp_dir):
    for subdir in dirs:
        # check folder name
        if subdir in target_subdirs:
            subdir_path = os.path.join(root, subdir)
            assets_path = os.path.join(subdir_path, 'assets')
            if os.path.exists(assets_path):
                # construct path
                target_assets_path = os.path.join(target_root_dir, subdir, 'assets')
                if not os.path.exists(target_assets_path):
                    os.makedirs(target_assets_path)
                for asset_root, asset_dirs, asset_files in os.walk(assets_path):
                    # get relative path
                    rel_path = os.path.relpath(asset_root, assets_path)
                    target_sub_path = os.path.join(target_assets_path, rel_path)
                    if not os.path.exists(target_sub_path):
                        os.makedirs(target_sub_path)
                    for asset_file in asset_files:
                        source_file = os.path.join(asset_root, asset_file)
                        target_file = os.path.join(target_sub_path, asset_file)
                        shutil.copy2(source_file, target_file)

# clean temp
shutil.rmtree(temp_dir)

print("Extraction completed!")