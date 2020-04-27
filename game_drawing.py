import numpy as np
from ipycanvas import Canvas, hold_canvas
from game_logic import get_next_stage


class GameOfLifePy:
    def __init__(self, stage, cell_size=10, live_color='white', dead_color='black', background_color='gray',
                 border_width=1.0):
        self.stage = stage
        self.cell_size = cell_size
        self.live_color = live_color
        self.dead_color = dead_color
        self.background_color = background_color
        self.border_width = border_width
        self.canvas = Canvas(width=self.stage.shape[0] * self.cell_size, height=self.stage.shape[1] * self.cell_size)
        display(self.canvas)

    def draw_stage(self):
        with hold_canvas(self.canvas):
            # draw live cells
            cells_index = np.where(self.stage)
            cells_x = cells_index[0] * self.cell_size
            cells_y = cells_index[1] * self.cell_size
            size_array = np.full(cells_x.shape, self.cell_size)
            self.canvas.fill_style = self.live_color
            self.canvas.fill_rects(cells_x, cells_y, size_array)
            # draw "border" of live cells
            if self.border_width != 0.0:
                self.canvas.line_width = self.border_width
                self.canvas.stroke_style = self.background_color
                self.canvas.stroke_rects(cells_x, cells_y, size_array)

            # draw dead cells
            cells_index = np.where(self.stage == False)
            cells_x = cells_index[0] * self.cell_size
            cells_y = cells_index[1] * self.cell_size
            size_array = np.full(cells_x.shape, self.cell_size)
            self.canvas.fill_style = self.dead_color
            self.canvas.fill_rects(cells_x, cells_y, size_array)
            # draw "border" of dead cells
            if self.border_width != 0.0:
                self.canvas.line_width = self.border_width
                self.canvas.stroke_style = self.background_color
                self.canvas.stroke_rects(cells_x, cells_y, size_array)

    def next_stage(self):
        self.stage = get_next_stage(self.stage)
