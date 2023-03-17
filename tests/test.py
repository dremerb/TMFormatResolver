#from tmformatresolver import get_color, change_format
from tmformatresolver import *

def printtest(string):
    print("=============================")
    tm = TMString(string)
    print("Original")
    print(string)
    print("str only")
    print(tm.string)
    print("html")
    print(tm.html)
    print("=============================")

def check_tm_string(data):
    tm = TMString(data[0])
    assert tm.string == data[1]
    assert tm.html == data[2]

def test_get_color():
    assert ("012", "") == get_color("012")
    assert ("340", "x") == get_color("34x")
    assert ("500", "jk") == get_color("5jk")
    assert ("", "gg") == get_color("ggg")

if __name__ == "__main__":
    teststr1 = ["$f00$f3b\u05d3\u05d5\u05d6\u03c2 $ga$nmgrebor$wn L\u0192s", "\u05d3\u05d5\u05d6\u03c2 amgreborn Lƒs", '<span style=";color:#f3b">\u05d3\u05d5\u05d6\u03c2 </span><span style=";color:#fff">a</span><span style="letter-spacing: -0.1em;font-size:smaller;;color:#fff">mgrebor</span><span style=";color:#fff">n Lƒs</span>']
    teststr2 = ["$w$999c¢¬$c60Cork$0aascrew", "c¢¬Corkscrew", '<span style="letter-spacing: -0.1em;font-size:smaller;;color:#999">c¢¬</span><span style="letter-spacing: -0.1em;font-size:smaller;;color:#c60">Cork</span><span style="letter-spacing: -0.1em;font-size:smaller;;color:#0aa">screw</span>']
    teststr3 = ["$CCC$idebil.$z$s$a00Cѳrk$0f1s$0a5crew", "debil.Cѳrkscrew", '<span style="letter-spacing: -0.1em;font-size:smaller;;color:#ccc">debil.</span><span style="letter-spacing: -0.1em;font-size:smaller;;color:#a00">Cѳrk</span><span style="letter-spacing: -0.1em;font-size:smaller;;color:#0f1">s</span><span style="letter-spacing: -0.1em;font-size:smaller;;color:#0a5">crew</span>']
    teststr4 = ["$o$i$a00K$a60a$aa0ck$0a0iest Kack$a00$a00y $g7 - Server 4", "Kackiest Kacky 7 - Server 4", '<span style=";color:#a00">K</span><span style=";color:#a60">a</span><span style=";color:#aa0">ck</span><span style=";color:#0a0">iest Kack</span><span style=";color:#a00">y </span><span style=";color:#fff">7 - Server 4</span>']
    teststr5 = ["$a#$312skand", "#skand", '<span style=";color:#aff">#</span><span style=";color:#312">skand</span>']
    teststr6 = ["$000deb$qil.", "debil.", '<span style=";color:#000">deb</span><span style=";color:#000">il.</span>']
    teststr7 = ["mög", "mög", '<span>mög</span>']
    teststr8 = ["$z$fff$o$n\u11ae\u11bb\u11b7$m$87b($111'$fd1\u00d7$eee\u0945$111'$87b)", "\u11ae\u11bb\u11b7('\u00d7\u0945')", '<span style=";color:#fff">ᆮᆻᆷ</span><span style="letter-spacing: -0.1em;font-size:smaller;letter-spacing: +0.1em;font-size:larger;;color:#87b">(</span><span style="letter-spacing: -0.1em;font-size:smaller;letter-spacing: +0.1em;font-size:larger;;color:#111">\'</span><span style="letter-spacing: -0.1em;font-size:smaller;letter-spacing:+0.1em;font-size:larger;;color:#fd1">×</span><span style="letter-spacing: -0.1em;font-size:smaller;letter-spacing: +0.1em;font-size:larger;;color:#eee">ॅ</span><span style="letter-spacing: -0.1em;font-size:smaller;letter-spacing: +0.1em;font-size:larger;;color:#111">\'</span><span style="letter-spacing: -0.1em;font-size:smaller;letter-spacing: +0.1em;font-size:larger;;color:#87b">)</span>']
    teststr9 = ["$fff$l[twitch.tv/aeqtm]ae\u0948q$e00neverlucky", "a\u0948qneverlucky", '<span style=";color:#fff">aeैq</span><span style=";color:#e00">neverlucky</span>']
    teststr10 = ["$fff$ltwitch.tv/aeqtm$lae\u0948q$e00neverlucky", "a\u0948qneverlucky", '<span style=";color:#fff">twitch.tv/aeqtmaeैq</span><span style=";color:#e00">neverlucky</span>']
    teststr11 = ["$l[kacky.gg]$fffIc\u0948e$z$s$f00neverlucky", "Icैeneverlucky", '<span style=";color:#fff">Icैe</span><span style="letter-spacing: -0.1em;font-size:smaller;;color:#f00">neverlucky</span>']
    teststr12 = ["$l$fffso\u0948$000$fffc$fffi$e00neverlucky \u00ab \u0442\u00b3", "soैcineverlucky « т³", '<span style=";color:#fff">soै</span><span style=";color:#fff">c</span><span style=";color:#fff">i</span><span style=";color:#e00">neverlucky « т³</span>']

    check_tm_string(teststr1)
    check_tm_string(teststr2)
    check_tm_string(teststr3)
    check_tm_string(teststr4)
    check_tm_string(teststr5)
    check_tm_string(teststr6)
    check_tm_string(teststr7)
    check_tm_string(teststr8)
    check_tm_string(teststr9)
    check_tm_string(teststr10)
    check_tm_string(teststr11)
    check_tm_string(teststr12)
