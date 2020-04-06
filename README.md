# Introduction 
This project if for vmware test. 
The project run a flask service to test two external endpoints and create a prometheus metrics.

# Getting Started
 1. Install Python 3:
       - Browse to: https://www.python.org/downloads/
       - On "Download the latest version for Windows", click "Download Python 3.7.2".
       - Run: python-3.7.2.exe
            - Click "Customize installation".
            - Optional Features: Accept default. Click "Next".
                 [X] Documentation
                 [X] pip
                 [X] tcl/tk and IDLE
                 [X] Python test suite
                 [X] py launcher   [X] for all users (requires elevation)
            - Advanced Options:
                 - Check "Install for all users"
                 - Check "Add Python to environment variables".
                 - Verify that it installs into: C:\Program Files (x86)\Python37-32
            - Click "Install".
            - Setup was successful. Click "Close".

       - Upgrade Python Package Manager:
            - Launch "Command Prompt" as Administrator.
            - Run:
                 ```
                 python -m pip install --upgrade pip
                 pip install --upgrade setuptools
                 ```

       - Install Python dependencies:
            - Download requirements.txt from https://slb-swt.visualstudio.com/central-sre/_git/sre-automation-py?path=%2Frequirements.txt&version=GBmaster
            - Launch "Command Prompt" as Administrator.
            - Run:
                 ```
                 python --version
                 pip install --upgrade --requirement requirements.txt
                 ```

       - To uninstall (OPTIONAL):
            - Click "Start   >   Settings   >   System   >   Apps & features".
              Click "Python 3.6.6 (32-bit)". Click "Uninstall".
              Click "Python Launcher". Click "Uninstall".
            - Delete C:\Users\KHaritmonds\AppData\Local\Programs\Python
              Note: Google library is in: c:\Users\KHaritmonds\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\google\cloud\
            - Delete c:\Program Files (x86)\Python37-32\
              Note: Google library is in: c:\Program Files (x86)\Python37-32\Lib\site-packages\google\cloud\

 2. Install PyCharm:
       - Browse to: https://www.jetbrains.com/pycharm/download/
       - On "Community", click "DOWNLOAD".
       - Run: pycharm-community-2018.3.2.exe

 3. Launch the project:
       - Click "File   >   Settings...".
            - Click "Project: vmware-test   >   Project Interpreter".
            - If you see the value of "Project Interpreter" is "<No interpreter>" then proceed with the next steps.
            - On "Project Interpreter", click Gear button, and click "Add...".
            - Click "(o) System Interpreter".
              Interpreter: C:\Program Files (x86)\Python37-32\python.exe
              Click "OK".
            - Click "OK".
       - Right click "Project   >   vmware-test   >   run.py", and then click "Run 'run-vmware-test'".
       - Browse to:   http://127.0.0.1:5000/metrics


# Test
Right click on test folder and click "Run 'py.test in test''"