from moviepy.editor import VideoFileClip
import sys, math, os, traceback, webbrowser

MAX_EMOJI_COUNT = 50
EMOJI_BLOCK_SZ = 32

def get_user_input(inp):
    if sys.version_info >= (3, 0):
        return input(inp)
    else:
        return raw_input(inp)

def main(argc, argv):
    if argc < 4:
        print('%s <input gif> <output directory> <emoji name> <max width emojis> [max height emojis]' % argv[0])
        return 1
    
    try:
        if not os.path.exists(argv[2]):
            os.makedirs(argv[2])
        max_w = int(argv[4])
        clip = VideoFileClip(argv[1])
        max_h = 0
        if argc == 6:
            max_h = int(argv[5])
            if max_h*max_w > MAX_EMOJI_COUNT:
                print('Emojis exceed limit of %d, emoji count is %d!' % (MAX_EMOJI_COUNT, max_h*max_w))
                option = get_user_input('Would you like to continue? (y/N): ').lower()
                if len(option) == 0 or option[0] != 'y':
                    return 1
        else:
            max_h = int(math.floor(MAX_EMOJI_COUNT / max_w))

        new_w = EMOJI_BLOCK_SZ * max_w
        new_h = EMOJI_BLOCK_SZ * max_h
        print('Rescaled size:', new_w, new_h)
        discord_cmd = ''
        idx = 0
        with open('%s/emoji_tester.html' % argv[2], 'wb') as fp:
            fp.write(b'<html><head><title>Emoji tester</title><meta charset="utf-8"></head><body>')
            fp.write(b'emoji testing, should look fine in discord<br>')
            for j in range(max_h):
                fp.write(b'<br>')
                for i in range(max_w):
                    c = clip.subclip((0)).resize((new_w, new_h))
                    print('i=%d, j=%d, max_w=%d, max_h=%d, x1=%d, y1=%d, x2=%d, y2=%d, w=%d, h=%d' % (i, j, max_w, max_h, i*EMOJI_BLOCK_SZ, j*EMOJI_BLOCK_SZ, (i+1)*EMOJI_BLOCK_SZ, (j+1)*EMOJI_BLOCK_SZ, c.w, c.h))
                    c.crop(x1=i*EMOJI_BLOCK_SZ, y1=j*EMOJI_BLOCK_SZ, x2=(i+1)*EMOJI_BLOCK_SZ, y2=(j+1)*EMOJI_BLOCK_SZ).write_gif('%s/%s%d.gif' % (argv[2], argv[3], idx))
                    fp.write(('<img src="%s%d.gif">' % (argv[3], idx)).encode('utf-8'))
                    discord_cmd += ':%s%d:' % (argv[3], idx)
                    idx += 1
                discord_cmd += '\n<br>'
            fp.write(b'<br>discord cmd<br>')
            fp.write(discord_cmd.encode('utf-8'))
            fp.write(b'</body></html>')

        print('\n', discord_cmd.replace('<br>', ''))
        webbrowser.get().open('file://' + os.path.abspath('%s/emoji_tester.html' % argv[2]))
    except:
        print("Unexpected error:", traceback.format_exc())
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
