# Tosca Execution Dashboard Generator

This repository contains the resources needed to generate a customized, professional Tosca execution dashboard. It parses results from multiple execution lists to provide test counts (Passed/Failed) and visual analytics via interactive pie charts.

## 📋 Contents

* **tosca_parser.py**: The core Python script that parses the raw log and generates the HTML dashboard.
* **GetResults.tcs**: A Tosca Shell script that navigates to the execution list folders and calls the individual result fetcher.
* **GetIndividualResult.tcs**: The specific action script that extracts the number of passed and failed test cases.
* **Results/**: The directory where the generated `.txt` logs and final `.html` report files are stored.
* **SchedulerBatchFile.bat**: Triggers `TCShell.exe`, handles workspace login, and initiates the `GetResults.tcs` script.
* **Execute.bat**: The main entry point. It runs the scheduler and ensures results are saved to `Results/ExecutionResult.txt`.

---

## 🚀 Workflow

The process follows a strictly automated pipeline to ensure data integrity and ease of use:

1. **Tosca Execution**: `Execute.bat` runs the scripts via TCShell.
2. **Log Generation**: Raw counts are saved to `ExecutionResult.txt`.
3. **Data Parsing**: `tosca_parser.py` reads the text file and calculates metrics.
4. **Visualization**: An HTML dashboard is generated with responsive pie charts.

---

## 📖 How to Use

1. **Execute Tests**: Double-click Execute.bat.
2. **Generate HTML Report**: Execute the following command
   ```python
   python tosca_parser.py
   ```

---

## 💻 Requirements

1. **Tricentis Tosca (v16 or higher recommended)**
2. **Python 3.x**


---

## ⚙️ Configuration

Before running, ensure the paths in `tosca_parser.py` match your local environment:

```python
# tosca_parser.py
PATHS = {
    "base_dir": r"D:\Tosca\Batch\Results",
    "input_file": "ExecutionResult.txt",
    "output_file": "ToscaReport.html"
}

```
---

## 📄 License

**© 2026 QASCRIPT | www.qascript.com**

All rights reserved.

