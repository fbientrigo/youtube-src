from manim import *

bt = 0.9 #base speed
q = 0.3 * bt #quick
m = 0.8 * bt #medium
s = 1.2 * bt #slow
ss = 1.6 * bt #slow slow

hipergeo = MathTex(r'{}_pF_q[a_p; b_q | x] = \sum_n \frac{\{a_p\}}{\{b_q\}} \frac{x^n}{n!}')

# write latex equation with manim library
class toHipergeometric(Scene):
    def construct(self):
        f1_left = MathTex(r'\frac{1}{1-x}')
        f1_right = MathTex(r'= \sum_{n=0}^\infty x^n')
        f1_right2 = MathTex(r'= \sum_n x^n')

        self.play(Write(f1_left))
        self.play(f1_left.animate.shift(0.8 * LEFT))
        f1_right.next_to(f1_left, RIGHT) # update positions
        f1_right2.next_to(f1_left, RIGHT)
        self.play(Write(f1_right))
        self.wait(s)

        self.play(Transform(f1_right, f1_right2))
        self.wait(s)

        self.clear()
        self.play(Write(hipergeo))
        self.wait(ss)
        self.play(FadeOut(hipergeo))

        # como se ve una hipergeometrica


        #es necesario el n factorial bajo el x, por tanto basta con multiplicar
        # arriba y abajo por este
        f1_sum = MathTex(r'\sum_n x^n')
        self.play(Write(f1_sum))
        f1_sum2 = MathTex(r'\sum_n \frac{n!}{n!}  x^n')
        self.play(Transform(f1_sum, f1_sum2))
        self.wait(q)

        # ahora es necesario tener Pochhammer
        f1_sum2_2 = MathTex(r'\sum_n n! \frac{x^n}{n!}')
        self.play(Transform(f1_sum, f1_sum2_2))
        self.wait(q)

        f1_sum2_2 = MathTex(r'n!')
        self.play(Transform(f1_sum, f1_sum2_2))
        self.play(f1_sum.animate.shift(0.8 * LEFT))
        fac_gam = MathTex(r'= \Gamma[n+1]')
        fac_gam.next_to(f1_sum, RIGHT)
        self.play(Write(fac_gam))
        self.wait(s) # ahora multiplicamos arriba y abajo

        fac_gam2 = MathTex(r'= \Gamma[n+1] \frac{\Gamma[1]}{\Gamma[1]}')
        fac_gam2.next_to(f1_sum, RIGHT)
        self.play(Transform(fac_gam, fac_gam2))
        fac_gam2 = MathTex(r'= \frac{\Gamma[n+1]}{\Gamma[1]} \Gamma[1]')
        fac_gam2.next_to(f1_sum, RIGHT)
        self.play(Transform(fac_gam, fac_gam2))
        self.wait(m) # aqui tenemos el pochhammer

        fac_gam2 = MathTex(r'= (1)_n \Gamma[1]')
        fac_gam2.next_to(f1_sum, RIGHT)
        self.play(Transform(fac_gam, fac_gam2))
        self.wait(q) #gamma de 1 vale 1

        fac_gam2 = MathTex(r'= (1)_n')
        fac_gam2.next_to(f1_sum, RIGHT)
        self.play(Transform(fac_gam, fac_gam2))
        self.wait(q) #gamma de 1 vale 1

        self.clear()

        # por tanto es posible ahora reemplazar en la serie
        f1_sum.shift(1*LEFT)
        f1_sum2 = MathTex(r'= \sum_n n! \frac{x^n}{n!}')
        f1_sum2.next_to(f1_left, RIGHT)
        self.play(Write(f1_left))
        self.play(Write(f1_sum2))
        f1_hyper = MathTex(r'= \sum_n (1)_n \frac{x^n}{n!}')
        f1_hyper.next_to(f1_left, RIGHT)
        self.play(Transform(f1_sum2, f1_hyper))
        self.wait(m)
        f1_hyper = MathTex(r'= {}_1F_0 [1; | x]')
        f1_hyper.next_to(f1_left, RIGHT)
        self.play(Transform(f1_sum2, f1_hyper))
        self.wait(ss)



class seriesconvergence(Scene):
    """ convergencia de una serie normal """
    def construct(self):
        # de los test mas comunes es ek de d'Alamberts, ratio test
        ratio_test = MathTex(r'\lim_{n \to \infty} |\frac{a_{n+1}}{ a_n }| = r')
        self.play(Write(ratio_test))
        self.wait(s)
        self.play(ratio_test.animation.shift(1.4*UP))
        self.wait(q)
        r_div = MathTex(r'r > 1')
        r_conv = MathTex(r'r < 1')
        r_1 = MathTex(r'r = 1')

        self.play(FadeOut(ratio_test))
        
        # integral test
        integral_test = MathTex(r'')
        self.play(Write(integral_test))
        self.wait(s)
        self.play(FadeOut(integral_test))


class convergence(Scene):
    """ convergencia de una hipergeoemtrica mediante las reglas"""
    def construct(self):
        self.play(Write(hipergeo))
        self.wait(m)
        self.play(hipergeo.animate.shift(2*UP))

        convergence_rule = MathTex(r'p = q + 1')
        convergence_rule.shift(2*LEFT)
        self.play(Write(convergence_rule))
        radius = MathTex(r'|x| < 1')
        radius.next_to(convergence_rule, RIGHT)
        self.play(Write(radius))
        self.wait(s)


