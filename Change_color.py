from qgis.core import QgsDataSourceUri
from qgis.utils import iface
import psycopg2
layer = iface.activeLayer()
renderer = layer.renderer()
symbol = renderer.symbol()
symbol.setColor(QColor(Qt.red))
symbol.setColor(QColor('red'))
symbol.setColor(QColor('#ff0000'))
symbol.setColor(QColor(255, 0, 0, 255))
layer.triggerRepaint()