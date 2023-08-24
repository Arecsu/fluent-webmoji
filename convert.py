import os
import json
import shutil
from pip._vendor.rich import progress

folder_path = './fluentui-emoji/assets'
json_file_name = "metadata.json"
output_path = './assets'

try:
    shutil.rmtree(output_path)
    print(f"Deleted {output_path} and its contents.")
except Exception as e:
    # print(f"Error: {e}")
    pass

os.mkdir(output_path)

skintones = ['Dark', 'Light', 'Medium',
             'Default', 'Medium-Dark', 'Medium-Light']
# the Default skintone doesn't have a unicode modifier. It's just the unicode value
skintones_with_modifiers = {
    'Light':          '1f3fb',
    'Medium-Light':   '1f3fc',
    'Medium':         '1f3fd',
    'Medium-Dark':    '1f3fe',
    'Dark':           '1f3ff'
}

'''
folders inside each emoji
3D     = Fluent Emoji 3D   ==> PNG 256x256
Color  = Fluent Emoji 3D   ==> SVG
Flat   = Fluent Emoji Flat ==> SVG
'''
# skipping 3D because I want to process the format with another app
# emojiTypes = ['3D', 'Color', 'Flat']
emojiTypes = ['Color', 'Flat']

# Get a list of subfolders in the specified directory
subfolders = [f for f in os.listdir(
    folder_path) if os.path.isdir(os.path.join(folder_path, f))]


def create_unicode_folder(unicode_value, srcPath, json_srcPath):
    unicode_folder_name = unicode_value.replace(' ', '-')
    destinationPath = os.path.join(output_path, unicode_folder_name)
    os.mkdir(destinationPath)
    # print(srcPath)
    # print(new_path)
    for emojiType in emojiTypes:
        srcPath_emojiType = os.path.join(srcPath, emojiType)
        srcFileNameWithExtension = os.listdir(srcPath_emojiType)[0]
        srcFileExtension = os.path.splitext(srcFileNameWithExtension)[-1]
        srcFilePath_emojiType = os.path.join(
            srcPath_emojiType, srcFileNameWithExtension)
        destinationFilePath_emojiType = os.path.join(
            destinationPath, emojiType.lower() + srcFileExtension)
        shutil.copy2(srcFilePath_emojiType, destinationFilePath_emojiType)

    # shutil.copytree(srcPath, new_path)
    # shutil.copy(json_srcPath, unicode_folder_name)


def process_folder_with_skintones(emoji_srcPath, emoji_unicode, emoji_with_skintone_unicode_group, json_file_path):
    for key in skintones_with_modifiers:
        for emoji_with_skintone_unicode in emoji_with_skintone_unicode_group:
            if skintones_with_modifiers[key] in emoji_with_skintone_unicode:
                emoji_with_skintone_srcPath = os.path.join(emoji_srcPath, key)
                create_unicode_folder(
                    emoji_with_skintone_unicode, emoji_with_skintone_srcPath, json_file_path)
    emoji_default_skintone_srcPath = os.path.join(emoji_srcPath, 'Default')
    create_unicode_folder(
        emoji_unicode, emoji_default_skintone_srcPath, json_file_path)


for folder in progress.track(subfolders):
    emoji_srcPath = os.path.join(folder_path, folder)
    json_file_path = os.path.join(emoji_srcPath, json_file_name)

    with open(json_file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    emoji_unicode = data["unicode"]
    hasUnicodeSkinTones = "unicodeSkintones" in data

    if hasUnicodeSkinTones:
        emoji_with_skintone_unicode_group = data["unicodeSkintones"]
        process_folder_with_skintones(
            emoji_srcPath, emoji_unicode, emoji_with_skintone_unicode_group, json_file_path)
    else:
        create_unicode_folder(emoji_unicode, emoji_srcPath, json_file_path)