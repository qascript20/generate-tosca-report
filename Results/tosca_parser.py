import re
import os
import sys
from datetime import datetime

def convert_tosca_log_to_html():
    # 1. DYNAMIC PATH CONFIGURATION
    # If an argument is passed, use it. Otherwise, look in the current folder.
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        # Default to the folder where the script is located
        base_dir = os.path.dirname(os.path.abspath(__file__))

    input_filename = "ExecutionResult.txt"
    output_filename = "ToscaReport.html"

    input_file_path = os.path.join(base_dir, input_filename)
    output_file_path = os.path.join(base_dir, output_filename)

    if not os.path.exists(input_file_path):
        print(f"Error: Could not find {input_filename} in {base_dir}")
        return

    # [Rest of the parsing logic remains the same...]
    try:
        with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            log_content = file.read()
    except Exception as e:
        print(f"Read Error: {e}")
        return

    passed = [int(x) for x in re.findall(r'NumberOfTestCasesPassed:\s*(\d+)', log_content)]
    failed = [int(x) for x in re.findall(r'NumberOfTestCasesFailed:\s*(\d+)', log_content)]
    generation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate HTML content strings...
    table_rows = ""
    chart_containers = ""
    chart_scripts = ""
    for i in range(len(passed)):
        idx = i + 1
        table_rows += f"<tr><td>Execution List #{idx}</td><td class='pass'>{passed[i]}</td><td class='fail'>{failed[i]}</td></tr>"
        chart_containers += f'<div class="chart-card"><h3>Execution List #{idx}</h3><div class="chart-wrapper"><canvas id="chart_{idx}"></canvas></div></div>'
        chart_scripts += f"new Chart(document.getElementById('chart_{idx}'), {{ type: 'pie', data: {{ labels: ['Passed', 'Failed'], datasets: [{{ data: [{passed[i]}, {failed[i]}], backgroundColor: ['#28a745', '#dc3545'], borderWidth: 2 }}] }}, options: {{ responsive: true, maintainAspectRatio: false }} }});"

    # HTML Template (truncated for brevity, include your QASCRIPT footer here)
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Tosca Execution Dashboard</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #f8f9fa; padding: 20px; }}
            .container {{ max-width: 1100px; margin: auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
            h1 {{ color: #0056b3; text-align: center; border-bottom: 3px solid #0056b3; padding-bottom: 10px; }}
            table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; }}
            th, td {{ padding: 12px; border: 1px solid #dee2e6; text-align: center; }}
            .pass {{ color: #28a745; font-weight: bold; }}
            .fail {{ color: #dc3545; font-weight: bold; }}
            .charts-grid {{ display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; }}
            .chart-card {{ border: 1px solid #eee; padding: 15px; width: 280px; text-align: center; }}
            .chart-wrapper {{ height: 200px; }}
            footer {{ text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; font-size: 0.9em; color: #666; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Tosca Execution Dashboard</h1>
            <p style="text-align:right; font-size:0.8em; color:#999;">Generated: {generation_time}</p>
            <table>
                <thead><tr><th>Execution Lists</th><th>Passed</th><th>Failed</th></tr></thead>
                <tbody>{table_rows}</tbody>
            </table>
            <div class="charts-grid">{chart_containers}</div>
            <footer>
                &copy; 2026 <strong>QASCRIPT</strong> | <a href="https://www.qascript.com/">www.qascript.com</a>
            </footer>
        </div>
        <script>{chart_scripts}</script>
    </body>
    </html>
    """

    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(html_template)
        print(f"Success: Report generated in {base_dir}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_tosca_log_to_html()