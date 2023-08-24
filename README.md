# Fluent Webmoji

This is basically Fluent Emoji from Microsoft.

The folder and file structure has been processed to easily request the URL of a specific emoji using their unicode value.

Additionally, every emoji has been rendered in WEBP.

The formats available:

- WEBP: 32x32, 64x64, 128x128
- SVG: source, and minified.

Featuring both Fluent Emoji families: 3D (Color) and Flat.

# Processing

Everything has been processed in the assets folder. To replicate the results or update it:

1. Fetch the icons from Microsoft's Fluent Emoji](https://github.com/microsoft/fluentui-emoji) repo (~130mb).

```bash
git clone https://github.com/microsoft/fluentui-emoji.git
```

2. Prerequisistes: 

- having `Python 3` (latest version) 
- `Imagemagick` in the system
- `inkscape`. Imagemagick uses it as the backend for SVG processing. Otherwise, it will fallback to a less capable SVG processor, which fails at rendering the SVGs.
- and `node` with NPM to install `svgo`. 

Install `svgo`:

```bash
npm -g install svgo
```

or use Yarn:
```bash
yarn global add svgo
```

3. Then:

```bash
python convert.py
./svg-processing.sh
``` 

`svg-processing.sh` minifies the SVGs and renders WEBP alternatives.