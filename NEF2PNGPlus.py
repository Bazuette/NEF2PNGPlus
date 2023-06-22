import os
import subprocess
from tkinter import filedialog
import sys

NEFnames = []
global irfanviewPath


def getNEFnames(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    NEFfiles = [f for f in files if f.endswith(".NEF")]
    return NEFfiles


def convertNEFtoPNG(fileList, input_folder, output_folder):

    if isinstance(fileList, list):
        possible_path = "C:\Program Files (x86)\IrfanView\i_view32.exe","C:\Program Files (x86)\IrfanView\i_view64.exe","C:\Program Files\IrfanView\i_view32.exe","C:\Program Files\IrfanView\i_view64.exe"

        for path in possible_path:
            if os.path.isfile(path) and os.path.exists(path):
                irfanviewPath = path

        try:
            irfanviewPath
        except:
            irfanviewPath = select_irfan_folder()


        do_converting(fileList, input_folder, output_folder, irfanviewPath)



def main():
    """Main function"""
    input_folder = select_input_folder()
    if not input_folder:
        print("No input folder selected.")
        return

    output_folder = select_output_folder()
    if not output_folder:
        print("No output folder selected.")
        return

    print(input_folder)
    print(output_folder)

    NEFnames = getNEFnames(input_folder)
    if not NEFnames:
        print("Warning: No NEF files found in the selected input folder.")
        return

    print("Starting Conversion...\n")
    convertNEFtoPNG(NEFnames, input_folder, output_folder)
    print("\nConversion completed!")


def select_input_folder():
    """Select the input folder using a file dialog"""
    input_folder = filedialog.askdirectory(title="Select Input Folder").replace('/', '\\')
    return input_folder


def select_output_folder():
    """Select the output folder using a file dialog"""
    output_folder = filedialog.askdirectory(title="Select Output Folder").replace('/', '\\')
    return output_folder


def select_irfan_folder():
    """Select the output folder using a file dialog"""

    irfanviewPath = filedialog.askopenfile(title="Select Irfan Folder").name
    print(irfanviewPath)
    return irfanviewPath


def do_converting(fileList, input_folder, output_folder, irfanviewPath):
    for f in fileList:
        input_path = os.path.join(input_folder, f)
        output_path = os.path.join(output_folder, os.path.splitext(f)[0] + " Converted.png")
        print("Converting:", input_path)
        try:
            subprocess.run([irfanviewPath, input_path, '/convert=',
                            output_path])
        except:
            print("Issue Found")


if __name__ == '__main__':
    main()
