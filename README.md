# DiscordEmojify
Turn gifs into emojis!

A quick and dirty script designed to create large "emojis" from gifs. The only requirements needed are python 2 and moviepy!

# Installation
`pip install -r requirements.txt`

# Usage
`python emojify.py <input gif path> <output gif directory> <base emoji name> <amount of "width" emojis>`

Example to create an 8x6 emoji block
`python emoji.py "C:\Path\Cat.gif" "C:\Path2\Output" "cat" 8`

The height block of the emojis is calulated by `MAX_EMOJI_COUNT / WIDTH` where `MAX_EMOJI_COUNT` is 50.


![alt text][logo]

[logo]: https://i.imgur.com/kYiBcdF.gif "Imgage example"
