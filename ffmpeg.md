# FFMPEG CheatSheet

### Auto overwrite output file
Add `-y` flag to overwrite output file if it already exists.

### Get video duration in seconds
```bash
ffprobe -i video.mov -show_entries format=duration -v quiet -of csv="p=0"
```

### Output a clip of input video
In this case we output a clip that starts at 10 seconds and ends at 15 minutes 15 seconds of the input video
```bash
ffmpeg -ss 00:00:10 -i input.mov -to 00:15:15 -c copy output.mov
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

### Convert multiple videos in folder (for Windows)
Open up power shell, then type `cmd`  
Then paste
```bash
for %i in (*.mov) do ffmpeg -i "%i" -f webm -c:v libvpx -b:v 2M -acodec libvorbis -auto-alt-ref 0 "%~ni.webm" -hide_banner
```
