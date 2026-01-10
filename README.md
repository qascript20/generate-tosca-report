# generate-tosca-report

This repository contains resources to generate a customized Tosca execution dashboard which contains results of different execution lists. It also provides number of tests passed, failed and pie charts for each execution list.

## Contents

- `GetResults.tcs` - jumps to the execution list folder on which we need to perform the action and calls the GetIndividualResult.tcs which will be performing the final action
- `GetIndividualResult.tcs` - gets number of test cases passed and failed for execution list
- `Results/` - directory where generated report files are stored
- `SchedulerBatchFile.bat` - triggers the TCShell.exe, will login into the workspace and triggers GetResults.tcs
- `Execute.bat` - triggers SchedulerBatchFile.bat file and stores results in Results/ExecutionList.txt 

## Usage

1. Double click the Execute.bat
2. ExecutionResult.txt file will be created in Results/ directory
3. Execute the following command to generate html report: python tosca_parser.py 

## Requirements

- Tricentis Tosca
- Python 
