from manim import *

class SummationPlot(Scene):
    def construct(self):
        x_start = -5
        x_end = 5
        dx = 0.1
        x_vals = np.arange(x_start, x_end+dx, dx)
        y_vals = np.zeros_like(x_vals)

        num_rects = 30
        delta_x = (x_end - x_start) / num_rects

        for i in range(num_rects):
            x = x_start + i * delta_x
            y = 1 / (1 + x**2)
            rect = Rectangle(height=y, width=delta_x, fill_opacity=0.8, fill_color=BLUE)
            rect.move_to(self.coords_to_point(x+delta_x/2, y/2))
            self.add(rect)

        graph = FunctionGraph(lambda x: 1 / (1 + x**2), x_min=x_start, x_max=x_end)
        graph.set_color(RED)
        self.add(graph)

        x_axis = NumberLine(x_range=[x_start, x_end, 1], length=10, include_numbers=True, numbers_to_show=range(x_start, x_end+1))
        x_axis.shift(2.5*DOWN)
        self.add(x_axis)

        y_axis = NumberLine(x_range=[0, 1, 0.5], length=5, include_numbers=True, numbers_to_show=[0, 0.5, 1])
        y_axis.rotate(PI/2)
        y_axis.next_to(x_axis, LEFT, buff=0)
        self.add(y_axis)
        
        self.wait()
