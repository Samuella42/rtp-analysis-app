from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import base64
from io import BytesIO

app = Flask(__name__)

def analyze_rtp_values(data, min_rtp=None, max_rtp=None, threshold=None):
    # Analiz fonksiyonu burada olacak
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        game_names = request.form.getlist('game_name')
        rtp_values = request.form.getlist('rtp_value')
        data = pd.DataFrame({
            'Oyun İsmi': game_names,
            'RTP Değeri': [float(rtp) for rtp in rtp_values]
        })
        analysis_result = analyze_rtp_values(data, min_rtp=96.0, max_rtp=98.0, threshold=97.0)
        return render_template('results.html', analysis_result=analysis_result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
