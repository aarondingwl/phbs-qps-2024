URL: https://github.com/aarondingwl/phbs-qps-2024.git

**Step 1: Set up a virtual environment**
It's a good practice to use a virtual environment to avoid conflicts with other Python packages. To create a virtual environment, follow these steps:

Navigate to the project folder:
cd phbs-qps-2024
Create a virtual environment:

On Windows:
python -m venv venv

On macOS/Linux:
python3 -m venv venv

**Step 2: Activate the virtual environment**
On Windows:
.\venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate
Once the environment is activated, you should see the (venv) prefix in your terminal prompt.

**Step 3: Install dependencies**
To install the required libraries for this project, run the following command inside the virtual environment:

pip install -r requirements.txt
The requirements.txt file should include all necessary packages such as pandas, numpy, matplotlib, requests, etc. If you don't have it, you can manually install the dependencies using:

pip install pandas numpy matplotlib requests

**Step 4: Run the code**
After setting up the environment and installing the dependencies, you can now run the code.

If you're working with Jupyter Notebook, you can start a Jupyter session by running:

jupyter notebook
Then open the notebook (e.g., fetch_us_cpi.ipynb) and run the cells.

If you're using Python scripts, you can run the script directly from the terminal:
python scripts/script_example.py
**Step 5: (Optional) Deactivate the virtual environment**
When you're done, you can deactivate the virtual environment by simply running:

deactivate
Troubleshooting
If you encounter any issues, ensure that all dependencies are installed correctly. You can also check the following:

Make sure your Python version is compatible (e.g., Python 3.7 or higher).
Ensure that Jupyter Notebook is installed if you're working with .ipynb files.
If the problem persists, feel free to open an issue in the repository and provide details about the error.
