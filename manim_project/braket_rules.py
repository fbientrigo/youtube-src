from manim import *

bt = 1.5 #base speed
q = 0.3 * bt #quick
m = 0.8 * bt #medium
s = 1.2 * bt #slow
ss = 1.6 * bt #slow slow

# write latex equation with manim library
class Multiplication(Scene):
    def construct(self):
        mult_rule = MathTex(r'\langle \alpha n + b \rangle = \frac{1}{|\alpha|} \langle  n + \frac{b}{\alpha} \rangle ')
        self.play(Write(mult_rule))
        self.wait(s)
        self.play(FadeOut(mult_rule))
        #partimos con la integral de la funcion de braket
        braket = MathTex(r'\langle \alpha n + b \rangle')
        self.play(Write(braket))
        self.wait(q)
        self.play(braket.animate.shift(0.8*LEFT))
        integral = MathTex(r'= \int_{0}^{\infty}  x^{\alpha n + b - 1} dx')
        integral.next_to(braket, RIGHT)
        self.play(Write(integral))
        self.play(FadeOut(braket))
        integral2 = MathTex(r'\int_{0}^{\infty}  x^{\alpha n + b - 1} dx')
        self.play(Transform(integral, integral2))
        self.wait(0.2*q)
        self.play(integral.animate.shift(LEFT))
        # centramos la ecuacion, ahora pasamos a indicar un cambio de variable
        self.play(integral.animate.shift(2*UP))
        self.wait(q)
        cambiovar = MathTex(r'x^{\alpha} = t')
        cambiovar.next_to(integral, DOWN)
        self.play(Write(cambiovar))
        self.wait(m)
        cambiovar2 = MathTex(r'\alpha x^{\alpha - 1} dx =dt')
        cambiovar2.next_to(cambiovar, DOWN)
        self.play(Write(cambiovar2))
        self.wait(s)
        cambiovar2_2 = MathTex(r'dx = \frac{dt}{\alpha x^{\alpha - 1}}')
        cambiovar2_2.next_to(cambiovar2, DOWN)
        self.play(Transform(cambiovar2, cambiovar2_2))
        self.wait(m)
        cambiovar_2 = MathTex(r'x = t^{\frac{1}{\alpha}}')	
        cambiovar_2.next_to(integral , DOWN)
        self.play(Transform(cambiovar, cambiovar_2))
        cambiovar2_2 = MathTex(r'dx = \frac{dt}{\alpha (t^{\frac{1}{\alpha}})^{\alpha - 1}}')
        cambiovar2_2.next_to(cambiovar, DOWN)
        self.play(Transform(cambiovar2, cambiovar2_2))
        self.wait(m)
        integral2 = MathTex(r'\int_{0}^{\infty} (t^{ \frac{1}{\alpha} })^{\alpha n + b - 1} \frac{dt}{\alpha (t^{\frac{1}{\alpha}})^{\alpha - 1}}')
        integral2.next_to(cambiovar, UP)
        self.play(Transform(integral, integral2))
        self.play(FadeOut(cambiovar2))
        self.play(FadeOut(cambiovar))
        self.play(integral.animate.shift(0.5*RIGHT))
        self.play(integral.animate.shift(2*DOWN))
        self.wait(m)
        # ahora solo trabajamos con la integral
        integral_2 = MathTex(r'\int_{0}^{\infty} t^{n + \frac{b}{\alpha} - \frac{1}{\alpha}} \frac{dt}{\alpha t^{1 - \frac{1}{\alpha}}} ')
        self.play(Transform(integral, integral_2))
        self.wait(s)
        integral_2 = MathTex(r'\frac{1}{\alpha}\int_{0}^{\infty} t^{n + \frac{b}{\alpha} - \frac{1}{\alpha} - (1 - \frac{1}{\alpha})} dt')
        self.play(Transform(integral, integral_2))
        self.wait(s)
        integral_2 = MathTex(r'\frac{1}{\alpha} \int_{0}^{\infty} t^{n + \frac{b}{\alpha} - \frac{1}{\alpha} - 1 + \frac{1}{\alpha}} dt')
        self.play(Transform(integral, integral_2))
        self.wait(s)
        integral_2 = MathTex(r'\frac{1}{\alpha} \int_{0}^{\infty} t^{n + \frac{b}{\alpha}  - 1 } dt')
        self.play(Transform(integral, integral_2))
        self.wait(ss)
        integralb = MathTex(r'= \langle n + \frac{b}{\alpha} \rangle')
        self.play(integral.animate.shift(LEFT))
        integralb.next_to(integral, RIGHT)
        self.play(Write(integralb))
        self.wait(ss)
        




