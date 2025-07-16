import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from fractions import Fraction

class BilinearInterpolationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bilinear Interpolation App")

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.load_button = tk.Button(self.master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.image = None

        self.master.bind("<Button-1>", self.interpolate_image_point)

        self.user_input_frame = tk.Frame(self.master)
        self.user_input_frame.pack()

        tk.Label(self.user_input_frame, text="Point 1 (x, y):").grid(row=0, column=0)
        tk.Label(self.user_input_frame, text="Point 2 (x, y):").grid(row=1, column=0)
        tk.Label(self.user_input_frame, text="Point 3 (x, y):").grid(row=2, column=0)
        tk.Label(self.user_input_frame, text="Point 4 (x, y):").grid(row=3, column=0)

        self.point1_entry = tk.Entry(self.user_input_frame)
        self.point2_entry = tk.Entry(self.user_input_frame)
        self.point3_entry = tk.Entry(self.user_input_frame)
        self.point4_entry = tk.Entry(self.user_input_frame)

        self.point1_entry.grid(row=0, column=1)
        self.point2_entry.grid(row=1, column=1)
        self.point3_entry.grid(row=2, column=1)
        self.point4_entry.grid(row=3, column=1)

        tk.Label(self.user_input_frame, text="RGB1:").grid(row=0, column=2)
        tk.Label(self.user_input_frame, text="RGB2:").grid(row=1, column=2)
        tk.Label(self.user_input_frame, text="RGB3:").grid(row=2, column=2)
        tk.Label(self.user_input_frame, text="RGB4:").grid(row=3, column=2)

        self.RGB1_entry = tk.Entry(self.user_input_frame)
        self.RGB2_entry = tk.Entry(self.user_input_frame)
        self.RGB3_entry = tk.Entry(self.user_input_frame)
        self.RGB4_entry = tk.Entry(self.user_input_frame)

        self.RGB1_entry.grid(row=0, column=3)
        self.RGB2_entry.grid(row=1, column=3)
        self.RGB3_entry.grid(row=2, column=3)
        self.RGB4_entry.grid(row=3, column=3)

        tk.Label(self.user_input_frame, text="Interpolation Point (x, y):").grid(row=6, column=0)
        self.interpolation_point_entry = tk.Entry(self.user_input_frame)
        self.interpolation_point_entry.grid(row=6, column=1)

        self.calculate_button = tk.Button(self.user_input_frame, text="Calculate", command=self.interpolate_user_input)
        self.calculate_button.grid(row=7, column=0, columnspan=4)

        self.points_display_frame = tk.Frame(self.master)
        self.points_display_frame.pack()

        tk.Label(self.points_display_frame, text="Points, RGB Values, and Colors").pack()

        self.points_table = tk.Text(self.points_display_frame, height=10, width=54)
        self.points_table.pack()

        self.color_canvas = tk.Canvas(self.master, height=50, width=200, bg="white")
        self.color_canvas.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        img = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=img)
        self.image_label.image = img

    def interpolate_image_point(self, event):
        if self.image is not None:
            x, y = event.x, event.y
            x_ratio = x / (self.image.width - 1)
            y_ratio = y / (self.image.height - 1)

            interpolated_pixel = self.bilinear_interpolation(x_ratio, y_ratio)
            print(f"Interpolated RGB at ({x_ratio}, {y_ratio}): {interpolated_pixel}")

            self.display_point_and_rgb((x_ratio, y_ratio), interpolated_pixel)
            self.display_color(interpolated_pixel)

    def interpolate_user_input(self):
        point1 = tuple(map(float, self.point1_entry.get().split(',')))
        point2 = tuple(map(float, self.point2_entry.get().split(',')))
        point3 = tuple(map(float, self.point3_entry.get().split(',')))
        point4 = tuple(map(float, self.point4_entry.get().split(',')))

        RGB1 = tuple(map(float, self.RGB1_entry.get().split(',')))
        RGB2 = tuple(map(float, self.RGB2_entry.get().split(',')))
        RGB3 = tuple(map(float, self.RGB3_entry.get().split(',')))
        RGB4 = tuple(map(float, self.RGB4_entry.get().split(',')))

        interpolation_point_str = self.interpolation_point_entry.get()

        try:
            interpolation_point = tuple(map(float, interpolation_point_str.split(',')))
        except ValueError:
            try:
                interpolation_point = tuple(float(Fraction(part)) for part in
                                            interpolation_point_str.replace('(', '').replace(')', '').split(','))
            except ValueError:
                print("Invalid input format for interpolation point.")
                return

        interpolated_pixel = self.bilinear_interpolation_manual(*interpolation_point, point1, point2, point3, point4,
                                                                RGB1, RGB2, RGB3, RGB4)
        print(f"Interpolated RGB at {interpolation_point}: {interpolated_pixel}")

        self.display_point_and_rgb(interpolation_point, interpolated_pixel)
        self.display_color(interpolated_pixel)

    def bilinear_interpolation(self, x, y):
        if self.image.mode != 'RGB':
            self.image = self.image.convert('RGB')

        image_array = np.array(self.image)
        x_coord = int(x * (self.image.width - 1))
        y_coord = int(y * (self.image.height - 1))

        interpolated_pixel = tuple(image_array[y_coord, x_coord, :])
        return interpolated_pixel

    def bilinear_interpolation_manual(self, x, y, point1, point2, point3, point4, RGB1, RGB2, RGB3, RGB4):
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3
        x4, y4 = point4

        lenght_1 =float(x-x1)
        lenght_2=float(x2-x)
        width_1=float(y-y1)
        width_2=float(y3-y)

        r = round(lenght_2 * width_2 * RGB1[0] + lenght_1 * width_2 * RGB2[0] +
                lenght_2 * width_1 * RGB3[0] + lenght_1 * width_1 * RGB4[0])

        g = round(lenght_2 * width_2 * RGB1[1] + lenght_1 * width_2 * RGB2[1] +
                  lenght_2 * width_1 * RGB3[1] + lenght_1 * width_1 * RGB4[1])

        b = round(lenght_2 * width_2 * RGB1[2] + lenght_1 * width_2 * RGB2[2] +
                  lenght_2 * width_1 * RGB3[2] + lenght_1 * width_1 * RGB4[2])

        return r, g, b

    def display_point_and_rgb(self, point, rgb):

        self.points_table.insert(tk.END, f"Point {point} - RGB: {rgb}\n")

    def display_color(self, rgb):

        rgb_int = tuple(int(value) for value in rgb)

        color_hex = "#{:02x}{:02x}{:02x}".format(*rgb_int)
        self.color_canvas.delete("all")
        self.color_canvas.create_rectangle(0, 0, 200, 50, fill=color_hex)


if __name__ == "__main__":
    root = tk.Tk()
    app = BilinearInterpolationApp(root)
    root.mainloop()