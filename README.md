# Paintings - Automatic Video

This is a Python script that downloads high resolution images from Google Arts and culture and creates a video with FFmpeg in which the images are animated with a Ken Burns Effect (zoom and pan).

## Dependencies

Download the most recent [dezoomify-rs](https://github.com/lovasoa/dezoomify-rs/releases) binary that will be used to download the images.

Also make sure that [FFmpeg](https://ffmpeg.org/) is installed and in your system path.

Finally, run `pip install -r requirements.txt` to get the necessary Python libraries.

> Disclaimer: this script was only tested on Linux, running it on Windows or Mac may fail

## Roadmap

| Feature                                                                                  | Status             |
|------------------------------------------------------------------------------------------|--------------------|
| Batch download images from [Google Arts and Culture](https://artsandculture.google.com/) | :heavy_check_mark: |
| Create video with Ken Burns Effect starting from dynamic zoom value                      | :x:                |
| Determine animation duration based on supplied audio                                     | :x:                |
