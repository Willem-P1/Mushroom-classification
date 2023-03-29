class Title(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        svg_path = "images/Mushroom.svg"
        svg = SVGMobject(svg_path,fill_color= WHITE).scale(2)
        title = Tex("Fungi or Foe").scale(2)
        
        willem = Tex('Willem Ploegstra', font_size = 32)
        martin = Tex('Martin Aviles', font_size = 32)
        jeremy = Tex('Jeremy Palmerio', font_size = 32)
        names = VGroup(martin, jeremy, willem)
        names.arrange_in_grid(rows=1, cols = 3, col_alignments='ccc').shift(DOWN*2)
       # svg_to_title = Transform(svg, title)
        #svg.move_to(ORIGIN)
        #self.play(Create(svg), run_time = 2)
        self.wait()
        #self.play(svg_to_title)
        self.play(Create(names))
        self.wait(3)