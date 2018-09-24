
from lcmap_tap.logger import log, exc_handler
from lcmap_tap.Controls import units
from lcmap_tap.RetrieveData import RowColumn, GeoAffine
from lcmap_tap.RetrieveData.retrieve_geo import GeoInfo
from lcmap_tap.RetrieveData.retrieve_chips import Chips
from lcmap_tap.Visualization.chipviewer_main import Ui_MainWindow_chipviewer

import sys
import time
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow

sys.excepthook = exc_handler


class ImageViewer(QtWidgets.QGraphicsView):
    image_clicked = QtCore.pyqtSignal(QtCore.QPointF)

    def __init__(self):
        super().__init__()

        self._zoom = 0

        self._empty = True

        self.scene = QtWidgets.QGraphicsScene(self)

        self._image = QtWidgets.QGraphicsPixmapItem()

        self._mouse_button = None

        self.view_holder = None

        self.rect = None

        self.scene.addItem(self._image)

        self.setScene(self.scene)

        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)

        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)

        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))

        self.setFrameShape(QtWidgets.QFrame.NoFrame)

    def has_image(self):
        return not self._empty

    def fitInView(self, scale=True, **kwargs):
        self.rect = QtCore.QRectF(self._image.pixmap().rect())

        if not self.rect.isNull():
            self.setSceneRect(self.rect)

            if self.has_image():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))

                self.scale(1 / unity.width(), 1 / unity.height())

                view_rect = self.viewport().rect()

                scene_rect = self.transform().mapRect(self.rect)

                factor = min(view_rect.width() / scene_rect.width(),
                             view_rect.height() / scene_rect.height())

                self.scale(factor, factor)

                self.view_holder = None

            self._zoom = 0

    def set_image(self, pixmap=None):
        # self._zoom = 0

        if pixmap and not pixmap.isNull():
            self._empty = False

            self._image.setPixmap(pixmap)

        else:
            self._empty = True

            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)

            self._image.setPixmap(QtGui.QPixmap())

        if self.view_holder is None:
            self.fitInView()

        else:
            view_rect = self.viewport().rect()

            scene_rect = self.transform().mapRect(self.view_holder)

            factor = min(view_rect.width() / scene_rect.width(),
                         view_rect.height() / scene_rect.height())

            self.scale(factor, factor)

    def wheelEvent(self, event: QtGui.QWheelEvent):
        if self.has_image():
            if event.angleDelta().y() > 0:
                # angleDelta is (+), wheel is rotated forwards away from the user, zoom in
                factor = 1.25
                self._zoom += 1

            else:
                # angleDelta is (-), wheel is rotated backwards towards the user, zoom out
                factor = 0.8
                self._zoom -= 1

            if self._zoom > 0:
                self.scale(factor, factor)

            elif self._zoom == 0:
                self.fitInView()

            else:
                self._zoom = 0

    def toggle_drag(self):
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)

        elif not self._image.pixmap().isNull():
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

    def mousePressEvent(self, event: QtGui.QMouseEvent):

        # 1 -> Left-click
        # 2 -> Right-click
        # 4 -> Wheel-click
        self._mouse_button = event.button()

        if event.button() == QtCore.Qt.RightButton:
            self.toggle_drag()

        if self._image.isUnderMouse() and event.button() == QtCore.Qt.LeftButton \
                and self.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            point = self.mapToScene(event.pos())

            self.image_clicked.emit(QtCore.QPointF(point))

        super(ImageViewer, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):

        # self.setDragMode(QtWidgets.QGraphicsView.NoDrag)

        super(ImageViewer, self).mouseReleaseEvent(event)


class ChipsViewerX(QMainWindow):
    def __init__(self, x, y, date, url, gui, geo, **params):
        super().__init__()

        self.chips = Chips(x, y, date, url, **params)

        self.gui = gui

        self.geo_info = geo

        self.pixel_image_affine = GeoAffine(ul_x=self.chips.grid['nw']['geo'].chip_coord.x,
                                            x_res=30,
                                            rot_1=0,
                                            ul_y=self.chips.grid['nw']['geo'].chip_coord.y,
                                            rot_2=0,
                                            y_res=-30)

        self.pixel_rowcol = GeoInfo.geo_to_rowcol(affine=self.pixel_image_affine, coord=self.geo_info.coord)

        self.ui = Ui_MainWindow_chipviewer()

        self.ui.setupUi(self)

        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        self.graphics_view = ImageViewer()

        self.ui.ScrollArea_viewer.setWidget(self.graphics_view)

        self.img = QImage(self.chips.rgb.data, self.chips.rgb.shape[1], self.chips.rgb.shape[0],
                          self.chips.rgb.strides[0],
                          QImage.Format_RGB888)

        self.img.ndarray = self.chips.rgb

        self.display_img()

        self.make_rect()

        self.init_ui()

        self.graphics_view.fitInView()

        self.ui.PushButton_zoom.clicked.connect(self.zoom_to_point)

        self.graphics_view.image_clicked.connect(self.update_rect)

    def init_ui(self):
        self.show()

    def display_img(self):
        """
        Show the ARD image

        Returns:

        """
        # Grab the current extent of the scene view so that the next image that gets opened is in the same extent
        self.graphics_view.view_holder = QtCore.QRectF(self.graphics_view.mapToScene(0, 0),
                                                       self.graphics_view.mapToScene(self.graphics_view.width(),
                                                                                     self.graphics_view.height()))

        try:
            self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

            self.pixel_map = QPixmap.fromImage(self.img)

            self.graphics_view.set_image(self.pixel_map)

            view_rect = self.graphics_view.viewport().rect()

            scene_rect = self.graphics_view.transform().mapRect(self.graphics_view.view_holder)

            factor = min(view_rect.width() / scene_rect.width(),
                         view_rect.height() / scene_rect.height())

            self.graphics_view.scale(factor, factor)

            # Set the scene rectangle to the original image size, which may be larger than the current view rect

            if not self.graphics_view.rect.isNull():
                self.graphics_view.setSceneRect(self.graphics_view.rect)

                # log.debug("self.graphics_view.rect used to set SceneRect")

        except AttributeError:
            pass

    def zoom_to_point(self):
        """
        Zoom to the selected point

        Returns:
            None

        """
        def check_upper(val, limit=0):
            for i in range(50, -1, -1):
                val_ul = val - i

                if val_ul > limit:
                    return val_ul

                elif val_ul < limit:
                    continue

                else:
                    return limit

        def check_lower(val, limit):
            for i in range(50, -1, -1):
                val_lr = val + i

                if val_lr < limit:
                    return val_lr

                elif val_lr > limit:
                    continue

                else:
                    return limit

        row_ul = check_upper(self.row)
        col_ul = check_upper(self.col)

        row_lr = check_lower(self.row, self.chips.rgb.shape[0])
        col_lr = check_lower(self.col, self.chips.rgb.shape[0])

        upper_left = QtCore.QPointF(col_ul, row_ul)
        bottom_right = QtCore.QPointF(col_lr, row_lr)

        rect = QtCore.QRectF(upper_left, bottom_right)

        view_rect = self.graphics_view.viewport().rect()

        scene_rect = self.graphics_view.transform().mapRect(rect)

        factor = min(view_rect.width() / scene_rect.width(),
                     view_rect.height() / scene_rect.height())

        self.graphics_view.scale(factor, factor)

        self.graphics_view.centerOn(self.current_pixel)

        # Arbitrary number of times to zoom out with the mouse wheel before full extent is reset
        self.graphics_view._zoom = 5

        self.graphics_view.view_holder = QtCore.QRectF(self.graphics_view.mapToScene(0, 0),
                                                       self.graphics_view.mapToScene(self.width(),
                                                                                     self.graphics_view.height()))

        # Set the scene rectangle to the original image size, which may be larger than the current view rect
        if not self.graphics_view.rect.isNull():
            self.graphics_view.setSceneRect(self.graphics_view.rect)

    def make_rect(self):
        """
        Create a rectangle on the image where the selected pixel location is located

        Returns:
            None

        """
        pen = QtGui.QPen(QtCore.Qt.yellow)
        pen.setWidthF(0.3)

        self.row = self.pixel_rowcol.row
        self.col = self.pixel_rowcol.column

        upper_left = QtCore.QPointF(self.col, self.row)
        bottom_right = QtCore.QPointF(self.col + 1, self.row + 1)

        self.current_pixel = QtWidgets.QGraphicsRectItem(QtCore.QRectF(upper_left, bottom_right))
        self.current_pixel.setPen(pen)

        self.graphics_view.scene.addItem(self.current_pixel)

    def update_rect(self, pos: QtCore.QPointF):
        """
        Get new row/col when image is clicked, draw a new rectangle at that clicked row/col location
        Args:
            pos: Contains row and column of the scene location that was clicked

        Returns:

        """
        # Only draw a new plot and update the rectangle if this option is selected
        if self.ui.RadioButton_plot.isChecked():
            # Remove the previous rectangle from the scene
            if self.current_pixel:
                self.graphics_view.scene.removeItem(self.current_pixel)

            pen = QtGui.QPen(QtCore.Qt.yellow)
            pen.setWidthF(0.3)

            self.row = int(pos.y())
            self.col = int(pos.x())

            upper_left = QtCore.QPointF(self.col, self.row)
            bottom_right = QtCore.QPointF(self.col + 1, self.row + 1)

            self.current_pixel = QtWidgets.QGraphicsRectItem(QtCore.QRectF(upper_left, bottom_right))
            self.current_pixel.setPen(pen)

            # self.graphics_view.scene.addRect(self.rect, pen)
            self.graphics_view.scene.addItem(self.current_pixel)

            time.sleep(1)

            self.update_plot()

    def update_plot(self):
        """
        Generate a new plot for the clicked point location

        Returns:
            None

        """
        self.pixel_rowcol = GeoInfo.geo_to_rowcol(affine=self.pixel_image_affine, coord=self.geo_info.coord)

        self.row = self.pixel_rowcol.row

        self.col = self.pixel_rowcol.column

        # Before generating the new plot, create a reference to the previously clicked date and subplot
        self.ax = self.gui.plot_window.b  # Subplot name

        # log.debug("self.ax = %s" % self.ax)

        self.date_x = self.gui.plot_window.x  # Date in ordinal datetime format, the x coordinate

        # log.debug("self.date_x = %s" % self.date_x)

        # Gather information to retrieve necessary data for the new plot
        rowcol = RowColumn(row=self.row, column=self.col)

        coords = GeoInfo.rowcol_to_geo(affine=self.pixel_image_affine,
                                       rowcol=rowcol)

        log.info("New point selected: %s" % str(coords))

        # Update the X and Y coordinates in the GUI with the new point
        if units[self.gui.selected_units]["unit"] == "meters":

            self.gui.ui.LineEdit_x1.setText(str(coords.x))

            self.gui.ui.LineEdit_y1.setText(str(coords.y))

        # Convert to lat/long before updating the coordinate text on the GUI
        else:
            _coords = GeoInfo.unit_conversion(coords)

            self.gui.ui.LineEdit_x1.setText(str(_coords.x))

            self.gui.ui.LineEdit_y1.setText(str(_coords.y))

        # Do the plotting and generate a new figure
        self.gui.check_values()

        self.gui.plot()

        """Need to determine the y-axis value for the new time series.  Can be done by determining the index within
        the new time-series of the x-axis (i.e. date) value from the previous time series """
        x_look_thru = {"obs_points": self.gui.plot_specs.dates_in[self.gui.plot_specs.qa_mask[
            self.gui.plot_specs.date_mask]],

                       "out_points": self.gui.plot_specs.dates_out[self.gui.plot_specs.fill_out],

                       "mask_points": self.gui.plot_specs.dates_in[~self.gui.plot_specs.qa_mask[
                           self.gui.plot_specs.date_mask]]
                       }

        y_look_thru = {"obs_points": self.gui.plot_specs.all_lookup[self.ax][0][self.gui.plot_specs.date_mask][
            self.gui.plot_specs.qa_mask[
                self.gui.plot_specs.date_mask]],

                       "out_points": self.gui.plot_specs.all_lookup[self.ax][0][~self.gui.plot_specs.date_mask][
                           self.gui.plot_specs.fill_out],

                       "mask_points": self.gui.plot_specs.all_lookup[self.ax][0][self.gui.plot_specs.date_mask][
                           ~self.gui.plot_specs.qa_mask[
                               self.gui.plot_specs.date_mask]]
                       }

        for key, x in x_look_thru.items():
            if self.date_x in x:
                log.info("Found date clicked %s in %s" % (self.date_x, key))

                self.x_series = x

                self.y_series = y_look_thru[key]

                break

        #: int: the location of the date in the new time series
        ind = np.where(self.x_series == self.date_x)

        #: the reflectance or index value for the new time series
        self.data_y = np.take(self.y_series, ind)

        # log.debug("Y-series value returned: %s" % self.data_y)

        # log.debug("From plot_window X: %s" % self.date_x)

        # log.debug("From plot_window Y: %s" % self.data_y)

        # Display the highlighted pixel in the new plot
        highlight = self.gui.plot_window.artist_map[self.ax][0]

        # log.debug("method update_plot, highlight=%s" % str(highlight))

        # highlight.set_data(self.date_x[0], self.data_y[0])
        highlight.set_data(self.date_x, self.data_y)

        self.gui.plot_window.canvas.draw()

        # Clear the list of previously clicked ARD observations because they can't be referenced in the new time-series
        self.gui.ui.ListWidget_selected.clear()