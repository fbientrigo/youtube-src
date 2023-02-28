from manim import *
import numpy as np

# write latex equation with manim library
class LatexEquation(Scene):
    def construct(self):
        # write latex equation
        latex = MathTex(r'\frac{d}{dx}f(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}')
        self.play(Write(latex))
        self.wait(2)

