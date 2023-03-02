from manim import *

class MyScene(Scene):
    def construct(self):
        # use the new LaTeX command in a MathTex object
        braket_example = MathTex(r"\langle {\alpha} \rangle")
        self.play(Write(braket_example))
        self.wait(0.4)

# class braket_graph(Scene): 
# tengo que hacer un grafico de la funcion de braket
# con esos cuadritos por debajo
