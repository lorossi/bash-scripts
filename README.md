# Bash scripts

This repo contains some bash script that I have developed during the years.
They don't do anything really important, but they help me automatize some of the things I do and I would be sad if they were somehow lost.

All of them are located in the `scripts` folder and can be run just by calling them in a POSIX terminal such as `./scriptname` or `sh scriptname`.

Some of them will need additional programs installed in your machine, while others will accept parameters.
Check the description here below to understand what they need and how they work.

## Scripts

### Binaural

Produces a binaural noise in your headphones (needed!).
Binaural tones are proven to help in certain circumstances, such as sleep, focus, or stimulating creativity.

This script requires `sox` in order to work.

Use:

- `binaural` will play a binaural tone with default settings
- `binaural -h` shows help and default settings
- `binaural [mode] [frequency] [harmonics]` will play a binaural tone with the specified settings. Refer to the help for more information on the parameters

### Makevideo

Produces a `GIF` and a `.mp4` video coded in x264 from a folder full of images in `.png` format.
All the images must be named in the format `0000000.png`, `0000001.png`, etc.

Use:

- `makevideo` will make a video from all the images in the `frames` subfolder
- `makevideo [path]` will make a video from all the images in the provided path

### Noise

Makes a mixture of white and pink noise to have some background sound.

This script requires `sox` in order to work.

Use:

- `noise` will play noise on a loop

### Rainbow

Gives a little color to your terminal.
Pipe any command into it or call a command with it to have a rainbow effect on the output.

Use:

- `command | rainbow` will print the output of the command with a rainbow effect

### Randomfile

Fills a file with random ASCII characters.

Use:

- `randomfile -h` show script help and default values
- `randomfile [path] [cols] [rows]` will fill the file at the provided path with random ASCII characters. The file will be `cols` columns wide and `rows` long.
  - if `cols` is not provided, it will be set to 80
  - if `rows` is not provided, it will be set to 40

### Uncommitted

Loops over all the subfolders of the current working directory and shows which of them contains uncommitted changes.

This script requires `git` in order to work.

Use:

- `uncommitted -h` shows help and default settings
- `uncommitted -s` or `uncommitted --show-clean` will show also the folders that don't have uncommitted changes. By default, only the folders with uncommitted changes are shown.
- `uncommitted -u` or `uncommitted --show-uninitialized` will show also the folders that are not git repositories. By default, only the folders that are git repositories are shown.
- `uncommitted -a` or `uncommitted --auto-commit` will auto commit and push all the uncommitted changes. By default, this option is not active.
- The parameters can be combined together

## Credits

This project and all the scripts inside it are distributed under MIT license.
