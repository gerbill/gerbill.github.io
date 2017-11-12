## BASH useful commands

##### Create a text file with no duplicate lines
```bash
sort input.txt | uniq > output.txt
```

##### Count lines in file
```bash
wc -l filename.txt
```

##### Archive a folder with TAR
```bash
tar -zcvf foldername.tar.gz foldername_tocompress
```

##### UnTAR an archive
```bash
tar -xf archive.tar -C /target/directory
```

##### Get directory size
```bash
du -hs /path/to/directory
```

##### Find a file without permission dinied errors
```bash
find /home/projects/ -name "*part_of_a_filename*"  2>&1 | grep -v "Permission denied"
```

##### Find a specific text inside files
```bash
grep -Ril "text-to-find-here" /path/to/folder/where/to/search
```
