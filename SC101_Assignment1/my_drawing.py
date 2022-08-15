"""
File: Let's go to beach!
Name: Rosy Huang
----------------------
TODO: This program shows my painting!
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Let's go to beach!

    This is my favorite free Line sticker! I'm going to go to Kenting this weekend and have a summer
    filled with beach memory. Let's go to beach and wear bikini together!
    """
    window = GWindow(width=500, height=500, title="Rosy's painting")

    hand_l_b = GOval(33, 85)
    hand_l_b.filled = True
    hand_l_b.fill_color = "black"
    hand_l_b.color = "black"
    window.add(hand_l_b, x=168, y=270)

    hand_r_b = GOval(33, 85)
    hand_r_b.filled = True
    hand_r_b.fill_color = "black"
    hand_r_b.color = "black"
    window.add(hand_r_b, x=307, y=270)

    hand_l = GOval(27, 83)
    hand_l.filled = True
    hand_l.fill_color = "papayawhip"
    hand_l.color = "papayawhip"
    window.add(hand_l, x=170, y=270)

    hand_r = GOval(27, 83)
    hand_r.filled = True
    hand_r.fill_color = "papayawhip"
    hand_r.color = "papayawhip"
    window.add(hand_r, x=310, y=270)

    pant = GRect(112, 102)
    pant.filled = True
    pant.fill_color = "paleturquoise"
    pant.color = "paleturquoise"
    window.add(pant, x=199, y=280)

    body_lower_b = GOval(115, 35)
    body_lower_b.filled = True
    body_lower_b.fill_color = "black"
    body_lower_b.color = "black"
    window.add(body_lower_b, x=198, y=283)

    body_lower = GOval(110, 30)
    body_lower.filled = True
    body_lower.fill_color = "papayawhip"
    body_lower.color = "papayawhip"
    window.add(body_lower, x=200, y=285)

    swimming_ring2 = GOval(206, 76)
    swimming_ring2.filled = True
    swimming_ring2.fill_color = "black"
    swimming_ring2.color = "black"
    window.add(swimming_ring2, x=147, y=228)

    face2_b = GOval(106, 110)
    face2_b.filled = True
    face2_b.fill_color = "black"
    face2_b.color = "black"
    window.add(face2_b, x=197, y=89)

    hair1_b = GOval(22, 43)
    hair1_b.filled = True
    hair1_b.fill_color = "black"
    hair1_b.color = "black"
    window.add(hair1_b, x=223, y=73)

    hair2_b = GOval(22, 43)
    hair2_b.filled = True
    hair2_b.fill_color = "black"
    hair2_b.color = "black"
    window.add(hair2_b, x=253, y=73)

    hair3_b = GOval(22, 43)
    hair3_b.filled = True
    hair3_b.fill_color = "black"
    hair3_b.color = "black"
    window.add(hair3_b, x=238, y=68)

    swimming_ring = GOval(200, 70)
    swimming_ring.filled = True
    swimming_ring.fill_color = "indianred"
    swimming_ring.color = "indianred"
    window.add(swimming_ring, x=150, y=230)

    face3_b = GOval(105, 55)
    face3_b.filled = True
    face3_b.fill_color = "black"
    face3_b.color = "black"
    window.add(face3_b, x=198, y=208)

    face = GRect(106, 100)
    face.filled = True
    face.fill_color = "black"
    face.color = "black"
    window.add(face, x=197, y=136)

    face = GRect(102, 100)
    face.filled = True
    face.fill_color = "papayawhip"
    face.color = "papayawhip"
    window.add(face, x=199, y=136)

    face2 = GOval(102, 105)
    face2.filled = True
    face2.fill_color = "papayawhip"
    face2.color = "papayawhip"
    window.add(face2, x=199, y=91)

    face3 = GOval(100, 50)
    face3.filled = True
    face3.fill_color = "papayawhip"
    face3.color = "papayawhip"
    window.add(face3, x=200, y=210)

    arc = GArc(313, 165, 280, 62)
    arc.filled = True
    arc.fill_color = "floralwhite"
    arc.color = "floralwhite"
    window.add(arc, x=203, y=218)

    arc2 = GArc(305, 160, 220, 58)
    arc2.filled = True
    arc2.fill_color = "floralwhite"
    arc2.color = "floralwhite"
    window.add(arc2, x=153, y=218)

    hair1 = GOval(15, 35)
    hair1.filled = True
    hair1.fill_color = "papayawhip"
    hair1.color = "papayawhip"
    window.add(hair1, x=225, y=75)

    hair2 = GOval(15, 35)
    hair2.filled = True
    hair2.fill_color = "papayawhip"
    hair2.color = "papayawhip"
    window.add(hair2, x=255, y=75)

    hair3 = GOval(15, 35)
    hair3.filled = True
    hair3.fill_color = "papayawhip"
    hair3.color = "papayawhip"
    window.add(hair3, x=240, y=70)

    mouth = GPolygon()
    mouth.add_vertex((230, 160))
    mouth.add_vertex((250, 170))
    mouth.add_vertex((270, 160))
    mouth.add_vertex((250, 150))
    mouth.filled = True
    mouth.fill_color = "yellow"
    window.add(mouth)

    mouth_line = GLine(230, 160, 270, 160)
    mouth_line.color = "black"
    window.add(mouth_line)

    eyeglass_l = GPolygon()
    eyeglass_l.add_vertex((210, 120))
    eyeglass_l.add_vertex((216, 140))
    eyeglass_l.add_vertex((239, 140))
    eyeglass_l.add_vertex((245, 120))
    eyeglass_l.filled = True
    eyeglass_l.fill_color = "black"
    window.add(eyeglass_l)

    eyeglass_r = GPolygon()
    eyeglass_r.add_vertex((255, 120))
    eyeglass_r.add_vertex((261, 140))
    eyeglass_r.add_vertex((284, 140))
    eyeglass_r.add_vertex((290, 120))
    eyeglass_r.filled = True
    eyeglass_r.fill_color = "black"
    window.add(eyeglass_r)

    eyeglass_line = GLine(200, 127, 300, 127)
    eyeglass_line.color = "black"
    window.add(eyeglass_line)

    pant_line1 = GLine(198, 300, 198, 382)
    pant_line1.color = "black"
    window.add(pant_line1)

    pant_line2 = GLine(312, 305, 312, 382)
    pant_line2.color = "black"
    window.add(pant_line2)

    pant_line3 = GLine(255, 340, 255, 382)
    pant_line3.color = "black"
    window.add(pant_line3)

    label = GLabel("走!")
    label.font = "-40"
    window.add(label, x=320, y=100)

    label2 = GLabel("去")
    label2.font = "-40"
    window.add(label2, x=100, y=100)

    label3 = GLabel("海")
    label3.font = "-40"
    window.add(label3, x=100, y=160)

    label4 = GLabel("邊")
    label4.font = "-40"
    window.add(label4, x=100, y=220)


if __name__ == '__main__':
    main()
