from manim import *
config.background_color = WHITE
config.frame_width = 2.2
config.frame_height = 3.3
config.pixel_width = 250
config.pixel_height = 375
import numpy as np

class Vector(Scene):
    def construct(self):
        arrowTipSize = 0.095
        arrow = Arrow(start=[-1, -3/2, 0], end=[1, 3/2, 0], color=PURE_RED, max_tip_length_to_length_ratio=arrowTipSize/(13**0.5)*2, buff=0)
        arrowBase = Arrow(start=[-1, -3/2, 0], end=[1, -3/2, 0], color=BLACK, max_tip_length_to_length_ratio=arrowTipSize, buff=0)
        alpha = MathTex(r"\alpha", color=BLACK).shift([-0.4, -1.2, 0])
        magnitude = MathTex(r"m", color=BLACK).shift([-0.25, 0.25, 0])
        magnitude.color = PURE_RED
        arc = Arc(0.4, 0, 0.982793723, arc_center=[-1,-3/2,0], color=BLACK)
        self.add(arc, arrowBase, arrow, alpha, magnitude)