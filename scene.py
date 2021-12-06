from manim import *



class Scene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        vector_i = Arrow3D(start=([0, 0, 0]), end=([2, 2, 2]), color = RED)
        vector_j = Arrow3D(start=([0, 0, 0]), end=([-7, 2, 2]), color = GREEN)
        ihat = Tex(r"[i]", color = RED).next_to(vector_i).rotate(PI/2, axis = X_AXIS)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("Cross Product")
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)
        self.play(FadeIn(axes, text3d))
        self.play(GrowFromPoint(vector_i, ([0,0,0])))
        self.play(GrowFromPoint(vector_j, ([0,0,0])))
        self.play(FadeIn(ihat))
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        