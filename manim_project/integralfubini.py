from manim import *
import numpy as np

class Fubini(Scene):
    def construct(self):
        # read equations from file
        with open("integralfubini.txt", "r") as f:
            equations = f.readlines()

        # write equations in Manim with transitions
        equation_mob = MathTex(equations[0].strip())
        self.play(Write(equation_mob))
        self.wait(2) #ecuacion a resolver



        for i in range(1, 7): # hasta la 6 y alli entra un cambio de variable
            new_mob = MathTex(equations[i])
            self.play(Transform(equation_mob, new_mob))
            self.wait(1)

        # change variable
        changevar1 = MathTex(equations[7])
        changevar2 = MathTex(equations[8])
        self.play(changevar1.animate.shift(2*UP))
        self.play(changevar2.animate.shift(3*UP))


        for i in range(9, 12): 
            new_mob = MathTex(equations[i])
            self.play(Transform(equation_mob, new_mob))
            self.wait(1)

            if i == 10:
                self.play(FadeOut(changevar1, duration=0.3))
                self.play(FadeOut(changevar2, duration=0.1))

        self.wait(0.2)

        # change variable
        changevar1 = MathTex(equations[12])
        changevar2 = MathTex(equations[13])
        self.play(changevar1.animate.shift(2*UP))
        self.play(changevar2.animate.shift(3*UP))


        new_mob = MathTex(equations[14].strip())
        self.play(Transform(equation_mob, new_mob))
        self.wait(1) #ecuacion a resolver

        self.play(FadeOut(changevar1, duration=0.3))
        self.play(FadeOut(changevar2, duration=0.3))

        for i in range(14, len(equations)): 
            new_mob = MathTex(equations[i])
            self.play(Transform(equation_mob, new_mob))
            self.wait(1)

