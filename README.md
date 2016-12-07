# pdf-image-to-text

A utility to convert a PDF made of images to text.

## Requirements

- ImageMagick (the library uses `convert` utility coming from ImageMagick lib)
- an OCR (tesseract-ocr >= 3.01 with *french* lang)

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
