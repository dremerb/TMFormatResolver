import re


__author__ = "Daniel Bremer"
__copyright__ = "Daniel Bremer"
__license__ = "WTFPL"

def get_color(colorkey):
    color_chars = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    color = "fff"
    if colorkey[0] in color_chars:
        color = colorkey[0] + color[1:]
    else:
        # consume first character, default color white, return unresolved chars
        return "", colorkey[1:]
    if len(colorkey) > 1 and colorkey[1] in color_chars:
        color = color[0] + colorkey[1] + color[2]
    else:
        # resolved color, unresolved keys
        return color, colorkey[1:]
    if len(colorkey) > 2 and colorkey[2] in color_chars:
        color = color[:2] + colorkey[2]
    else:
        # resolved color, unresolved keys
        return color, colorkey[2]
    # resolved color
    return color, ""


def change_format(formatters, color):
    #   | style | width
    # 0b 1 1 1 1 0 0
    #    o i t s w n
    bit_span_map = {
        0b000001: "letter-spacing: -0.1em;font-size:smaller",  # $n - narrow
        0b000010: "letter-spacing: +0.1em;font-size:larger",  # $w - wide font
        0b000100: "text-shadow: 1px 1px 1px #000",  # $s - drop shadow
        0b001000: "text-transform:uppercase",  # $t - uppercase text
        0b010000: "font-style:italic",  # $i - italic font
        0b100000: "font-weight:bold",  # $o - bold font
    }

    style = ""
    for key, htmlstyle in bit_span_map.items():
        if formatters & key:
            style += htmlstyle + ";"
    return f'</span><span style="{style};color:#{color}">'


class TMString:
    def __init__(self, tmstring):
        self.string = re.sub(
            r"\$[0-9a-f]{1,3}|\$[wnoitsgzml$]", "", tmstring, flags=re.IGNORECASE
        )

        # replace color codes with html
        htmlstr = ""

        formatters = 0
        color = "fff"

        #   | style | width
        # 0b 1 1 1 1 0 0
        #    o i t s w n
        key_bit_map = {
            "n": 0b000001,  # $n - narrow
            "w": 0b000001,  # $w - wide font
            "s": 0b000001,  # $s - drop shadow
            "t": 0b000001,  # $t - uppercase text
            "i": 0b000001,  # $i - italic font
            "o": 0b000001,  # $o - bold font
            "m": 0b000011,  # reset all styles
            # $z and $g are handled explicitly, as they influence color as well
        }

        # handle link removal
        if "$l" in tmstring.lower():
            # link is present. can have four forms "$l.*$l", "$l[.*].*$l" or both variants without closing "$l"
            # remove "$l"/"$L" with split(). if "$l[.*].*$l" is not used, we cannot safely remove the link :/
            # In that case, leave the link in there. Makes the nick ugly, but can't really change that
            parts = re.split(r"\$l|\$L", tmstring)
            newtmstring = ""
            for block in parts:
                if block != "" and block[0] == "[":
                    # tmstring contains at least "$l[.*]". remove [.*] part.
                    # count=1 makes sure we only replace the link
                    block = re.sub(r"\[[^]]*\]", "", block, count=1)
                newtmstring += block
            tmstring = newtmstring

        parts = tmstring.split("$")
        for loopidx, block in enumerate(parts):
            # escape "<" and ">" to prevent injections
            block = block.replace("<", "&lt;").replace(">", "&gt;")
            if loopidx == 0 and tmstring[0] == "$" and block == "":
                # `string` starts with a $, `split("$")` yields a "" as first list element
                continue
            if loopidx == 0 and tmstring[0] != "$":
                # `string` starts without any formatters, so skip evaluation of this block
                htmlstr += block
                continue
            if block == "":
                # must have been a $$. Insert $
                htmlstr += "&#36;"
                continue
            if block[0].lower() in key_bit_map.keys():
                formatters ^= key_bit_map[block[0].lower()]
                htmlstr += change_format(formatters, color) + block[1:]
                continue
            if block[0].lower() == "g":
                # reset color
                color = "fff"
                htmlstr += change_format(formatters, color) + block[1:]
                continue
            if block[0].lower() == "z":
                # reset color and formatters
                color = "fff"
                formatters = 0
                htmlstr += change_format(formatters, color) + block[1:]
                continue
            # must either be color or ignored
            newcolor, remainder = get_color(block[:3].lower())
            color = newcolor if newcolor != "" else color
            htmlstr += change_format(formatters, color) + remainder + block[3:]

        # remove all empty spans
        self.html = re.sub(
            r'<span( style="[a-z0-9\.;:#\s+-]*")*><\/span>',
            "",
            "<span>" + htmlstr + "</span>",
        )
