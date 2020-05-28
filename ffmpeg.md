# FFMPEG CheatSheet

### Auto overwrite output file
Add `-y` flag to overwrite output file if it already exists.

### Get video duration in seconds
```bash
ffprobe -i video.mov -show_entries format=duration -v quiet -of csv="p=0"
```

### Output first N seconds oF a video
In this case we output first 1000 seconds
```bash
ffmpeg -sseof -1000 -i input.mov output.mov
```

### Concat video files
```bash
ffmpeg -safe 0 -f concat -i files.txt -vcodec copy -acodec aac -strict -2 -b:a 384k output.mov
```
where files.txt contains the following:
```
file ./input_1.mov
file ./input_2.mov
file ./input_3.mov
```
