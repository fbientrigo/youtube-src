from manim import *


# write latex equation with manim library
class Presentation(Scene):
    def construct(self):
        # write first integral problem

        # Gamma
        gamma = MathTex(r'\Gamma(n+1) = n! ')
        self.play(Write(gamma))
        self.wait(1.4)
        gammaz = MathTex(r'\Gamma(z)')
        self.play(Transform(gamma, gammaz))
        self.wait(0.8)
        # definition of gamma function via integral
        gamma_integral = MathTex(r'\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} dt ')
        self.play(Transform(gamma, gamma_integral))
        self.wait(1.6)
        gamma_factorial = MathTex(r'\Gamma(z+1)= z \Gamma(z)')
        self.play(Transform(gamma, gamma_factorial))
        self.wait(1.6)
        self.play(FadeOut(gamma))
        self.wait(1)

        # se comporta similar al factorial
        gamma_factorial = MathTex(r'\Gamma(n+1)=')
        gamma_factorial.shift(2*LEFT)
        gamma_factorial2 = MathTex(r'n \Gamma(n)')
        gamma_factorial2.next_to(gamma_factorial, RIGHT)
        self.play(Write(gamma_factorial))
        self.wait(1)
        self.play(Write(gamma_factorial2))
        self.wait(1.1)
        gamma_factorial2_2 = MathTex(r'n (n-1) \Gamma(n-1)')
        gamma_factorial2_2.next_to(gamma_factorial, RIGHT)
        self.play(Transform(gamma_factorial2, gamma_factorial2_2))
        self.wait(1)
        gamma_factorial2_3 = MathTex(r'n (n-1) (n-2) \Gamma(n-2)')
        gamma_factorial2_3.next_to(gamma_factorial, RIGHT)
        self.play(Transform(gamma_factorial2, gamma_factorial2_3))
        self.wait(0.3)
        gamma_factorial2_4 = MathTex(r'n (n-1) (n-2) \cdots (2) \Gamma(2)')
        gamma_factorial2_4.next_to(gamma_factorial, RIGHT)
        self.play(Transform(gamma_factorial2, gamma_factorial2_4))
        self.wait(0.4)
        gamma_factorial2_5 = MathTex(r'n (n-1) (n-2) \cdots (2) (1)')
        gamma_factorial2_5.next_to(gamma_factorial, RIGHT)
        self.play(Transform(gamma_factorial2, gamma_factorial2_5))
        self.wait(0.4)
        gamma_factorial2_6 = MathTex(r'n!')
        gamma_factorial2_6.next_to(gamma_factorial, RIGHT)
        self.play(Transform(gamma_factorial2, gamma_factorial2_6))
        self.wait(1.8)
        self.clear()

       # recordar del video de foubini donde describimos
        gamma = MathTex(r'\Gamma(1/2) = \sqrt{\pi}')
        self.play(Write(gamma))
        self.wait(1.5)
        self.clear()

        # entonces tenemos la gamma y este objeto como los mas improtantes
        indicador = MathTex(r'\phi_n = \frac{(-1)^n}{n!}')
        self.play(Write(indicador))
        self.play(indicador.animate.shift(2*LEFT))
        self.wait(0.7)
        self.play(gammaz.animate.shift(2*RIGHT))
        self.wait(1.6)
        self.clear()


class braket_defi(Scene):
    def construct(self):
        braket = MathTex(r'\langle \alpha \rangle')
        self.play(Write(braket))
        self.wait(0.8)
        braket_def = MathTex(r'= \int_{0}^{\infty} x^{\alpha - 1} dx')
        self.play(braket.animate.shift(2*LEFT))
        braket_def.next_to(braket, RIGHT)
        self.play(Write(braket_def))



class Expansion(Scene):
    def construct(self):
        # son importantes pues a la hora de expandir en serie obtendremos estos objetos:
        euler_x2 = MathTex(r'e^{-x^2}')
        self.play(Write(euler_x2))
        self.wait(0.4)
        self.play(euler_x2.animate.shift(LEFT))
        # escribir la expansión al lado derech
        euler_x2_expansion = MathTex(r'= \sum_{n=0}^\infty \frac{(-1)^n}{n!} x^{2n}')
        # write the expansion to the right side
        euler_x2_expansion.next_to(euler_x2, RIGHT)
        self.play(Write(euler_x2_expansion))
        self.wait(1.6)
        euler_x2_expansion2 = MathTex(r'= \sum_{n=0}^\infty \phi_n x^{2n}')
        euler_x2_expansion2.next_to(euler_x2, RIGHT)
        self.play(Transform(euler_x2_expansion, euler_x2_expansion2))
        self.wait(2)
        self.play(FadeOut(euler_x2_expansion))
        self.clear()

        # Braket integral
        braket_integral_example = MathTex(r'\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}')
        self.play(Write(braket_integral_example))
        self.wait(2)
        braket_integral_example2 = MathTex(r' \int_{-\infty}^{\infty} e^{-x^2} dx')
        self.play(Transform(braket_integral_example, braket_integral_example2))
        self.wait(2)
        braket_integral_example2 = MathTex(r'2\int_{0}^{\infty} e^{-x^2} dx')
        self.play(Transform(braket_integral_example, braket_integral_example2))
        self.wait(1)
        self.play(braket_integral_example.animate.shift(2*DOWN))
        self.wait(1)
        # escrib la expansion
        expansion = MathTex(r'e^{-x^2}= \sum_{n=0}^\infty \phi_n x^{2n}')
        expansion.shift(2*UP)
        self.play(Write(expansion))
        self.wait(1)
        # utilizada la expansion 
        braket_integral_example2 = MathTex(r'2\int_{0}^{\infty}\sum_{n=0}^\infty \phi_n x^{2n} dx')
        self.play(Transform(braket_integral_example, braket_integral_example2))
        #desaparecer la expansion
        self.play(FadeOut(expansion))
        self.wait(1)
        #entonces aqui se se integra cada objeto
        braket_integral_example2 = MathTex(r'2\sum_{n=0}^\infty \int_{0}^{\infty} \phi_n x^{2n} dx')
        self.play(Transform(braket_integral_example, braket_integral_example2))
        braketdef = MathTex(r'\langle \alpha \rangle = \int_{0}^{\infty} x^{\alpha - 1} dx')
        braketdef.shift(2*UP)
        self.play(Write(braketdef))
        self.wait(1)
        braket_integral_example2 = MathTex(r'2\sum_{n=0}^\infty \phi_n  \langle 2n +1 \rangle')
        self.play(Transform(braket_integral_example, braket_integral_example2))
        self.play(FadeOut(braketdef)) 
        self.wait(1)
        regla_brakets = MathTex(r'\sum_n \phi_n f(n) \langle \alpha + n \rangle')
        regla_brakets.shift(2*UP)
        regla_brakets2 = MathTex(r'=\Gamma(-n) f(n) |_{n=-\alpha}')
        regla_brakets2.next_to(regla_brakets, RIGHT)
        self.play(Write(regla_brakets))
        self.wait(1)
        self.play(Write(regla_brakets2))
        self.wait(1.09)
        # escribir una segunda regla
        regla_brakets3 = MathTex(r'\langle \beta n + \alpha \rangle = \frac{1}{|\beta|} \langle  n + \frac{\alpha}{\beta} \rangle ')
        regla_brakets3.shift(2*DOWN)
        self.play(Write(regla_brakets3))
        # modificamos la integral con esta regla primero
        braket_integral_example2 = MathTex(r'2\sum_{n=0}^\infty \phi_n \frac{1}{2}\langle n + \frac{1}{2} \rangle')
        self.play(Transform(braket_integral_example, braket_integral_example2))
        self.wait(0.39)
        braket_integral_example2 = MathTex(r'\sum_{n=0}^\infty \phi_n \langle n + \frac{1}{2} \rangle')
        self.play(FadeOut(regla_brakets3))
        self.wait(0.39)
        self.play(Transform(braket_integral_example, braket_integral_example2))
        self.wait(0.59)
        # ahora modificamos la integral con regla de brakets
        braket_integral_example2 = MathTex(r'\Gamma(-n) |_{n = -\frac{1}{2}}')
        self.play(Transform(braket_integral_example, braket_integral_example2))
        self.wait(0.39)
        self.play(FadeOut(regla_brakets))
        self.play(FadeOut(regla_brakets2))
        self.wait(0.69)
        braket_integral_example2 = MathTex(r'\Gamma(\frac{1}{2})')
        self.play(Transform(braket_integral_example, braket_integral_example2))
        self.wait(0.59)
        braket_integral_example2 = MathTex(r'\sqrt{\pi}')
        self.play(Transform(braket_integral_example, braket_integral_example2))
        self.wait(0.89)
