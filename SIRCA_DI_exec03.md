# Curso Sistemas Inteligentes e Robótica em Ciências Agrárias

## Módulo Infraestrutura de dados


# 0. Introdução

O objectivo deste exercício é preparar a infraestrutura de dados para armazenar 
os registos realizados por sensores instalados no terreno. 

Neste caso, a abordagem inclui a criação de uma máquina virtual na cloud, onde 
os dados serão guardados, e depois acedidos para visualização ou download. Neste 
exemplo, utilizaremos as recomendações do ChatGPT. Serão apresentadas as prompts
submetidas ao chatbot, as respostas e as acções tomadas para a implementação
da infraestrutura.

O chat completo está disponível em [https://chatgpt.com/share/6838814a-2d08-800b-9861-42a3aa2d9e4b](https://chatgpt.com/share/6838814a-2d08-800b-9861-42a3aa2d9e4b).

# 1. Obter o delineamento para a infraestrutura

A primeira decisão a ser resolvida é se infraestrutura será local ou cloud. Vamos
assumir que é na cloud. Existem muitos serviços cloud que podemos usar para essa
finalidade. Ver uma lista, por exemplo, [aqui](https://github.com/cloudcommunity/Cloud-Free-Tier-Comparison). Vamos pedir orientação sobre os passos para implementar uma máquina 
virtual com o serviço Amazon AWS:

```
I want to create a vm in amazon aws. The goal is to configure it to store soil 
sensor data through time. Can you guide me on the steps to do it?
```

A resposta inclui uma descrição genérica dos passos:

```

🧭 Overview of Steps

    1. Create an AWS Account (if you don’t already have one)

    2. Launch an EC2 instance (your VM)

    3. Set up storage (e.g., attach an EBS volume or use S3)

    4. Secure the VM (SSH, firewall rules, IAM)

    5. Install required software (e.g., database, server tools)

    6. Design data ingestion pipeline (e.g., API, MQTT, or direct DB insert)

    7. Test and monitor the system

```

Esta parte é seguida da descrição detalhada dos passos. Estes podem ser consultados no [chat](https://chatgpt.com/share/6838814a-2d08-800b-9861-42a3aa2d9e4b), mas vamos rever alguns dos passos mais importantes.

# 2. Instalação do software necessário

É possível, ao criar a VM, usar uma imagem que seja já baseada num sistema linux
pré-configurado. Isso é muito usual em aplicações em que cada VM está dedicada a 
apenas um ou poucos serviços, por exemplo, o alojamento de uma base de dados.
Neste caso, seleccionámos um sistema Ubuntu.

Após a criação da máquina, o primeiro passo é fazer a actualização do software:

```bash
sudo apt update && sudo apt upgrade -y
```

A aplicação será implementada com python, pelo que é necessário instalar o seguinte 
software:
- python
- pip: gestor de packages do python
- mariadb-server: gestor de bases de dados relacionais
- nginx: software ervidor web

O software pode ser instalado com o seguinte comando:
```bash
sudo apt install -y python3 python3-pip mariadb-server nginx

```

# 3. Configuração da base de dados MariaDB

Para configurar a segurança da base de dados, correr:
```bash
sudo mysql_secure_installation
```

Depois, criar a base de dados. Para isso, fazer login:
```bash
sudo mariadb
```
e executar o seguinte SQL
```SQL
CREATE DATABASE soil_data;
USE soil_data;
CREATE TABLE readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    sensor_id VARCHAR(100),
    temperature FLOAT,
    moisture FLOAT,
    ph FLOAT
);

```

É também necessário configurar um utilizador e password para a base de dados.
```SQL
GRANT ALL PRIVILEGES ON soil_data.* TO app_user@localhost IDENTIFIED BY 'app_passwd';

FLUSH PRIVILEGES;
```
# 4. Configuração adicional do servidor

Para fazer com que a aplicação em python interagisse com a base de dados MariaDB
de forma correcta, foi necessária fazer a  configuração de pacotes adicionais do 
sistema operativo. Estes foram instalados por tentativa/erro, e em resultado de 
pesquisas online.

As seguintes configurações são necessárias:

```bash
sudo apt-get install libmysqlclient-dev
pip3 install flask flask-mysqldb
```
# 5. Criar a aplicação Flask

Flask é uma framework de python que permite criar aplicações web de forma simples.
Suporta também a implementação de APIs.

Podemos escrever o script `app.py`, que implementa o API:

```python

from flask import Flask, request
import MySQLdb
from datetime import datetime

app = Flask(__name__)
db = MySQLdb.connect(host="localhost", user="youruser", passwd="yourpass", db="soil_data")

# esta parte gera o serviço de submissão dos dados via API
@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    cur = db.cursor()
    cur.execute("INSERT INTO readings (timestamp, sensor_id, temperature, moisture, ph) VALUES (%s, %s, %s, %s, %s)", 
                (datetime.utcnow(), data["sensor_id"], data["temperature"], data["moisture"], data["ph"]))
    db.commit()
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

Para executar, podemos correr noutro terminal
```bash
curl -X POST -H "Content-Type: application/json" -d '{"sensor_id":"1","temperature":23.5,"moisture":40.2,"ph":6.8}' http://10.17.131.42:5000/submit

```
**Atenção**: no comando anterior, é necessário alterar o IP do servidor.


# 6. Implementação de um dashboard para visualizar os dados

Podemos pedir ao ChatGPT para nos ajudar a criar um dashboard:
```
can you add a web dashboard for data views?
```
Na resposta, é proposto combinar as seguintes componentes:

- Flask (your existing app)

- HTML + Bootstrap (for the frontend)

- Chart.js (for interactive charts)

A **arquitectura** do sistema será a seguinte:
```
Soil Sensor → Flask API → MariaDB
                            ↓
                       Flask Web UI
                            ↓
                       User Browser
```

A implementação do dashboard será baseada na seguinte estrutura de directorias
e ficheiros:
```
soil-dashboard/
├── app.py
├── templates/
│   └── dashboard.html
```
## 6.1 Actualizar a `app.py` 

É necessário adicionar a função que cria o dashboard ao script da aplicação.

```python
from flask import Flask, request, render_template
import MySQLdb
from datetime import datetime

app = Flask(__name__)
db = MySQLdb.connect(host="localhost", user="youruser", passwd="yourpass", db="soil_data", autocommit=True)

# esta parte gera o serviço de submissão dos dados via API
@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    cur = db.cursor()
    cur.execute("INSERT INTO readings (timestamp, sensor_id, temperature, moisture, ph) VALUES (%s, %s, %s, %s, %s)",
                (datetime.utcnow(), data["sensor_id"], data["temperature"], data["moisture"], data["ph"]))
    return "OK", 200

# esta é a parte nova de código que gera o dashboard
@app.route("/dashboard")
def dashboard():
    cur = db.cursor()
    cur.execute("SELECT timestamp, sensor_id, temperature, moisture, ph FROM readings ORDER BY timestamp ASC LIMIT 100")
    rows = cur.fetchall()
    timestamps = [row[0].strftime("%Y-%m-%d %H:%M:%S") for row in rows]
    temperatures = [row[2] for row in rows]
    moistures = [row[3] for row in rows]
    phs = [row[4] for row in rows]
    return render_template(
        "dashboard.html",
        timestamps=timestamps,
        temperatures=temperatures,
        moistures=moistures,
        phs=phs
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```
## 6.2. Criar o ficheiro templates/dashboard.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>Soil Sensor Dashboard</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body class="p-4 bg-light">
  <div class="container">
    <h2 class="mb-4">Soil Sensor Dashboard</h2>

    <!-- Temperature Chart -->
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">Temperature (°C)</h5>
        <canvas id="tempChart"></canvas>
      </div>
    </div>

    <!-- Moisture Chart -->
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">Moisture (%)</h5>
        <canvas id="moistureChart"></canvas>
      </div>
    </div>

    <!-- pH Chart -->
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">pH</h5>
        <canvas id="phChart"></canvas>
      </div>
    </div>
  </div>

  <script>
    const labels = {{ timestamps|tojson }};
    const temperatures = {{ temperatures|tojson }};
    const moistures = {{ moistures|tojson }};
    const phs = {{ phs|tojson }};

    const createChart = (canvasId, label, data, color) => {
      new Chart(document.getElementById(canvasId), {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: label,
            data: data,
            borderColor: color,
            backgroundColor: color + '33',
            tension: 0.2,
            fill: true,
            pointRadius: 1
          }]
        },
        options: {
          responsive: true,
          scales: {
            x: { title: { display: true, text: 'Timestamp' } },
            y: { beginAtZero: false }
          }
        }
      });
    };

    createChart('tempChart', 'Temperature (°C)', temperatures, 'red');
    createChart('moistureChart', 'Moisture (%)', moistures, 'blue');
    createChart('phChart', 'pH', phs, 'green');
  </script>
</body>
</html>
```

# 7. Simulação de submissão de dados com um novo script `send_data.py`

Podemos pedir ao ChatGPT para criar um script `send_data.py` que simula a submissão de dados
a partir de um sensor. Este deverá submeter dados a cada 30 segundos. Podemos
usar a seguinte prompt:

```python
import requests
import random
import time
from datetime import datetime

API_URL = "http://<your-vm-ip>:5000/submit"  # Replace with your actual VM IP

def generate_fake_data(sensor_id):
    return {
        "sensor_id": sensor_id,
        "temperature": round(random.uniform(15.0, 30.0), 2),  # °C
        "moisture": round(random.uniform(20.0, 80.0), 2),     # %
        "ph": round(random.uniform(5.5, 7.5), 2)              # pH
    }

def send_data():
    sensor_id = "sensor01"
    while True:
        payload = generate_fake_data(sensor_id)
        print(f"[{datetime.now()}] Sending: {payload}")
        try:
            response = requests.post(API_URL, json=payload)
            print(f"→ Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(30)  # wait 30 seconds before sending next reading

if __name__ == "__main__":
    send_data()

```

Para executar, 
```bash
python3 send_data.py
```

# 8. Descarregar dados
Podemos pedir para adicionar à nossa webapp a funcionalidade de descarregamento de
dados, adicionando um formulário.

Usamos a seguinte prompt:

```
add a button to the dashboard to download data, by filtering time and parameter
```

Será necessário actualizar `app.py`:


```python
from flask import send_file
import io
import csv
from datetime import datetime

@app.route("/download", methods=["POST"])
def download():
    start = request.form.get("start")
    end = request.form.get("end")
    parameter = request.form.get("parameter")

    query = """
        SELECT timestamp, sensor_id, temperature, moisture, ph
        FROM readings
        WHERE timestamp BETWEEN %s AND %s
        ORDER BY timestamp ASC
    """

    cur = db.cursor()
    cur.execute(query, (start, end))
    rows = cur.fetchall()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["timestamp", "sensor_id", parameter])

    param_index = {"temperature": 2, "moisture": 3, "ph": 4}[parameter]

    for row in rows:
        writer.writerow([row[0], row[1], row[param_index]])

    output.seek(0)

    filename = f"sensor_data_{parameter}_{start}_to_{end}.csv"
    return send_file(io.BytesIO(output.getvalue().encode()),
                     mimetype="text/csv",
                     as_attachment=True,
                     download_name=filename)
```
E adicionar `templates/dashboard.html`

```html
<div class="card mb-4">
  <div class="card-body">
    <h5 class="card-title">Download Data</h5>
    <form method="POST" action="/download" class="row g-3">
      <div class="col-md-3">
        <label for="start" class="form-label">Start Time</label>
        <input type="datetime-local" class="form-control" name="start" required>
      </div>
      <div class="col-md-3">
        <label for="end" class="form-label">End Time</label>
        <input type="datetime-local" class="form-control" name="end" required>
      </div>
      <div class="col-md-3">
        <label for="parameter" class="form-label">Parameter</label>
        <select name="parameter" class="form-select" required>
          <option value="temperature">Temperature (°C)</option>
          <option value="moisture">Moisture (%)</option>
          <option value="ph">pH</option>
        </select>
      </div>
      <div class="col-md-3 d-flex align-items-end">
        <button type="submit" class="btn btn-primary w-100">Download CSV</button>
      </div>
    </form>
  </div>
</div>
```




## Resumo

Neste exercício, utilizámos AI para 
- gerar código para carregar dados
- calcular estatísticas básicas
- criar gráficos de estatísticas univariadas e bivariadas
- calcular a ACP



