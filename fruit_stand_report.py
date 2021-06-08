# PDF libraries (reportlab)
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

# Get Data
# Format into a .pdf report
report_body = SimpleDocTemplate()
report_data = Paragraph()
report_chart = Table()