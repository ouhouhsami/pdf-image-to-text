# pdf-image-to-text

A utility to convert a PDF made of images to text.

## Requirements

- ImageMagick (the library uses `convert` utility coming from ImageMagick lib)
- an OCR (tesseract-ocr >= 3.01 with *french* lang)
- Python 3

## Install

(pip 9.0.1 works)

```
pip install pdf-image-to-text --process-dependency-links
```

## Usage

Common use (output to a json file)

```
pdf-image-to-text.py <file.pdf> > <file.txt>
```


Generic use (output to standard output)

```
pdf-image-to-text.py <file.pdf>
```

License : BSD (3-Clause)
