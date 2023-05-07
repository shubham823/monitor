from flask import Flask, render_template
import psutil
import matplotlib.pyplot as plt
import io
import base64
import yaml
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

@app.route('/')
def index():
    with open('servers.yml') as f:
        servers = yaml.safe_load(f)

    charts = []

    for server in servers:
        server_name = server['name']
        server_type = server['type']
        disk_path = server['disk_path']

        disk_usage = psutil.disk_usage(disk_path)
        total_space = disk_usage.total
        used_space = disk_usage.used
        free_space = disk_usage.free
        percent_used = (used_space / total_space) * 100
        labels = ['Used Space', 'Free Space']
        sizes = [percent_used, 100 - percent_used]
        fig = plt.figure(figsize=(4, 4))
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        # Render the figure as an image in memory
        canvas = FigureCanvas(fig)
        png_output = io.BytesIO()
        canvas.print_png(png_output)
        png_output.seek(0)

        # Encode the image as a base64 string
        png_data = base64.b64encode(png_output.getvalue()).decode('utf-8')

        chart = f"data:image/png;base64,{png_data}"
        charts.append({'server_name': server_name, 'server_type': server_type, 'chart': chart})

    return render_template('index.html', charts=charts)

if __name__ == '__main__':
    app.run(debug=True)
