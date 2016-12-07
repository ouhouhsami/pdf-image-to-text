#!/usr/local/bin/python3
import getopt
import glob
import json
import os
import re
import subprocess
import sys

from PIL import Image
import pyocr
import pyocr.builders


tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]

langs = tool.get_available_languages()
lang = langs[langs.index('fra')]


def main(argv):
    cmd = "convert -density 300 %s %s.png" % (argv[0], argv[0])
    run = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = run.communicate()
    text = ''
    for file_path in glob.glob("%s*.png" % argv[0]):
        txt = tool.image_to_string(
            Image.open(file_path),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        os.remove(file_path)
        text = text+'\n'+txt
    sys.stdout.write(text)


if __name__ == "__main__":
    main(sys.argv[1:])