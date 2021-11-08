from pathlib import Path
from os import listdir
import openpyxl

from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)

from openpyxl.chart.trendline import Trendline
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.drawing.line import LineProperties
from openpyxl.chart.text import RichText
from openpyxl.drawing.text import Paragraph, ParagraphProperties, CharacterProperties, Font, Color
from openpyxl.chart.data_source import NumFmt
from openpyxl.chart.axis import ChartLines

from .add_to_template import Template
template = Template()