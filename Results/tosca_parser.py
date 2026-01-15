import re
import os
from datetime import datetime

# ==========================================================
# 1. CONFIGURATION - Update your settings here
# ==========================================================
PATHS = {
    "base_dir": r"D:\Tosca\Batch\Results",
    "input_file": "ExecutionResult.txt",
    "output_file": "ToscaReport.html"
}

BRANDING = {
    "company": "QASCRIPT",
    "website": "https://www.qascript.com/",
    "display_url": "www.qascript.com"
}
# ==========================================================

def convert_tosca_log_to_html():
    input_path = os.path.join(PATHS["base_dir"], PATHS["input_file"])
    output_path = os.path.join(PATHS["base_dir"], PATHS["output_file"])

    if not os.path.exists(input_path):
        print(f"Error: Could not find {input_path}")
        return

    try:
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as file:
            log_content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Extracting Data
    passed = [int(x) for x in re.findall(r'NumberOfTestCasesPassed:\s*(\d+)', log_content)]
    failed = [int(x) for x in re.findall(r'NumberOfTestCasesFailed:\s*(\d+)', log_content)]
    gen_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate content for table and charts
    table_rows = ""
    chart_containers = ""
    chart_scripts = ""

    for i in range(len(passed)):
        idx = i + 1
        p, f = passed[i], failed[i]
        
        table_rows += f"<tr><td>Execution List #{idx}</td><td class='pass'>{p}</td><td class='fail'>{f}</td></tr>"
        
        chart_containers += f"""
        <div class="chart-card">
            <h3>Execution List #{idx}</h3>
            <div class="chart-wrapper"><canvas id="chart_{idx}"></canvas></div>
        </div>"""
        
        chart_scripts += f"""
        new Chart(document.getElementById('chart_{idx}'), {{
            type: 'pie',
            data: {{
                labels: ['Passed', 'Failed'],
                datasets: [{{
                    data: [{p}, {f}],
                    backgroundColor: ['#28a745', '#dc3545'],
                    borderWidth: 2
                }}]
            }},
            options: {{ responsive: true, maintainAspectRatio: false }}
        }});"""

    # HTML Template
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Tosca Execution Dashboard</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #f8f9fa; padding: 20px; }}
            .container {{ max-width: 1000px; margin: auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
            h1 {{ color: #0056b3; text-align: center; border-bottom: 3px solid #0056b3; padding-bottom: 10px; }}
            .time {{ text-align: right; font-size: 0.8em; color: #888; margin-bottom: 20px; }}
            table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; }}
            th, td {{ padding: 12px; border: 1px solid #dee2e6; text-align: center; }}
            th {{ background: #f1f3f5; }}
            .pass {{ color: #28a745; font-weight: bold; }}
            .fail {{ color: #dc3545; font-weight: bold; }}
            .charts-grid {{ display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; }}
            .chart-card {{ border: 1px solid #eee; border-radius: 8px; padding: 15px; width: 280px; text-align: center; }}
            .chart-wrapper {{ height: 200px; }}
            footer {{ margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; text-align: center; color: #666; font-size: 0.9em; }}
            footer a {{ color: #0056b3; text-decoration: none; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Tosca Execution Dashboard</h1>
            <div class="time">Generated: {gen_time}</div>
            
            <table>
                <thead>
                    <tr><th>Execution Lists</th><th>Test Cases Passed</th><th>Test Cases Failed</th></tr>
                </thead>
                <tbody>{table_rows}</tbody>
            </table>

            <div class="charts-grid">{chart_containers}</div>

            <footer>
                &copy; {datetime.now().year} <strong>{BRANDING['company']}</strong> | 
                <a href="{BRANDING['website']}" target="_blank">{BRANDING['display_url']}</a>
                <br>All rights reserved.
            </footer>
        </div>
        <script>{chart_scripts}</script>
    </body>
    </html>
    """

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"Dashboard successfully generated at: {output_path}")

if __name__ == "__main__":
    convert_tosca_log_to_html()