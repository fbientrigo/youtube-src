import manim as mn
import numpy as np


def experiment1(x, y, z, color=mn.WHITE):
    """Draw a braket with the given color."""
    return mn.VGroup(
        mn.Line(x, y, color=color),
        mn.Line(y, z, color=color),
        mn.Line(x, z, color=color)
    )


# write latex equation with manim library
class Presentation(mn.Scene):
    def construct(self):
        # write first integral problem

        # Gamma
        gamma = mn.MathTex(r'\Gamma(n+1) = n! ')
        # definition of gamma function via integral
        gamma_integral = mn.MathTex(r'\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} dt ')

        # se comporta similar al factorial
        gamma_factorial = mn.MathTex(r'\Gamma(n+1) = n \Gamma(n)')

        # nos permite escribir la función gamma como un factorial más general
        # por ejemplo para números no enteros:
        gamma_app_example_01 = mn.MathTex(r'\int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi} ')
        # generate a manim code for the above integral, doing the change of variables
        gamma_app_example_02 = mn.MathTex(r'I =  \int_{-\infty}^\infty e^{-x^2} dx = 2 \int_{0}^\infty e^{-x^2} dx')
        gamma_changeofvariable = mn.MathTex(r't = x^2')
        gamma_changeofvariable2 = mn.MathTex(r'dt = 2xdx')
        gamma_changeofvariable3 = mn.MathTex(r'dx = \frac{1}{2} \frac{dt}{\sqrt{t}}')
        gamma_changeofvariable4 = mn.MathTex(r' 2 \int_{0}^\infty e^{-x^2} dx = 2 \int_{0}^\infty e^{-t}\frac{1}{2} \frac{dt}{\sqrt{t}}')
        gamma_changeofvariable4_2 = mn.MathTex(r' = \int_{0}^\infty e^{-t} \frac{dt}{\sqrt{t}} ')
        gamma_changeofvariable4_3 = mn.MathTex(r' = \int_{0}^\infty e^{-t} t^{-1/2}dt')

        gamma_app_example_1 = mn.MathTex(r'\Gamma(1/2) = \sqrt{\pi}')

        # por ejemplo para números negativos no enteros
        gamma_app_example_2 = mn.MathTex(r'\Gamma(-1/2) = \sqrt{\pi}i')

        indicador = mn.MathTex(r'\frac{(-1)^n}{n!}')

        # Braket integral
        braket_integral_example = mn.TextMobject(r'\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}')

        braket_integral_example.scale(0.5)

        # show them using manim, in the order they are written
        self.play(mn.Write(gamma))
        self.play(mn.Write(indicador))
        self.play(mn.Write(braket_integral_example))
