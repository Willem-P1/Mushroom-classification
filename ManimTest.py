from manim import *
from manim.mobject.svg.svg_mobject import SVGMobject
class Title(Scene):
    def construct(self):
        svg = SVGMobject('images/Mushrooms.svg', color = WHITE)
        title = Tex("Fungi or Foe").scale(2)
        svg_to_title = Transform(svg, title)
        svg.move_to(ORIGIN)
        self.play(Create(svg), run_time = 2)
        self.wait()
        self.play(svg_to_title)
        self.wait(3)