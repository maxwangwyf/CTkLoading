import customtkinter as ctk
import math
class LoadingAnimation:
    def __init__(self, root):
        self.root = root
        self.window = ctk.CTkToplevel(root)
        self.window.overrideredirect(True)
        self.window.attributes("-alpha", 0.5)
        self.window.attributes("-topmost", True)
        # 设置窗口大小
        self.window_width = 200
        self.window_height = 200
        self.center_window()

        # 创建 Canvas 组件
        self.canvas = ctk.CTkCanvas(self.window, width=self.window_width, height=self.window_height,bg="#CFCFCF",highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # 圆圈参数
        self.angle = 0
        self.radius = 50
        self.center = (self.window_width // 2, self.window_height // 2)
        self.line_length = 20

        self.lines = []
        self.create_loading_animation()
        self.animate()
        self.window.grab_set()

    def center_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.window.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def create_loading_animation(self):
        for i in range(12):
            angle = i * 30
            x1 = self.center[0] + self.radius * math.cos(math.radians(angle))
            y1 = self.center[1] + self.radius * math.sin(math.radians(angle))
            x2 = self.center[0] + (self.radius - self.line_length) * math.cos(math.radians(angle))
            y2 = self.center[1] + (self.radius - self.line_length) * math.sin(math.radians(angle))
            line = self.canvas.create_line(x1, y1, x2, y2, fill="yellow", width=3)
            self.lines.append(line)
    def animate(self):
        self.angle += 10
        if self.angle >= 360:
            self.angle = 0

        for i, line in enumerate(self.lines):
            self.canvas.delete(line)
            angle = (i * 30 + self.angle) % 360
            x1 = self.center[0] + self.radius * math.cos(math.radians(angle))
            y1 = self.center[1] + self.radius * math.sin(math.radians(angle))
            x2 = self.center[0] + (self.radius - self.line_length) * math.cos(math.radians(angle))
            y2 = self.center[1] + (self.radius - self.line_length) * math.sin(math.radians(angle))
            self.lines[i] = self.canvas.create_line(x1, y1, x2, y2, fill="black", width=3)

        self.window.after(100, self.animate)

    def close(self):
        self.window.grab_release()
        self.window.destroy()