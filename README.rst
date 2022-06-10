Trade Analytics
================

|made-with-python|

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

|Documentation Status|

.. |Documentation Status| image:: https://readthedocs.org/projects/ansicolortags/badge/?version=latest
   :target: http://ansicolortags.readthedocs.io/?badge=latest

This dashboard is developed to serve expert traders as well as newcomers to help them predict the trends of top 4-5 companies in each of the major sectors and hence help them with their investment. This is part of the final project for ECE 229: Computational Data Science & Product Development at UCSD.

If you're interested in entering the market and want to get a head start, this dashboard is for you.We hope this brings our users a unique interactive experience, and allows them to invest and diversify better.

.. image:: https://github.com/anish52/trade-analytics/blob/main/dashboard.png?sanitize=true

Installation
------------

Requires python 3.7+

Some main third-party modules:

- ta 0.10.0
- TAcharts 0.0.29
- voila 0.3.5
- yfinance 0.1.70
- ipyvuetify 1.8.2
- ipywidgets 7.6.5

Clone the repository using:

```
https://github.com/anish52/trade-analytics.git
```

Create a python virtual environment

```
python -m venv env
```


Activate the environment

```
source  env/bin/activate
```

Install dependencies

```
pip install requirements.txt
```

Deactivate when done making changes

```
deactivate
```

Usage
------------
To run this webapp on your server, go inside the 'dashboard' directory where this repository sits, and type in your terminal:

```
python app.py
```

This will launch the app locally on your machine. Visiting the url as shown will bring you to home screen of our dashboard. You will need to upload the 'template.json' file in the dashboard (top-right corner) to visit all the tabs.


Documentation
-------------
The documentation has been created using Sphinx Documentation and is available under 'docs' directory. 
You can find the docs at '/docs/build/html/index.html'.


Code Coverage Tests
--------------------
To run the code coverage tests on your server, go inside the 'tests' directory where this repository sits, and type in your terminal:

```
pytest --cov-report term-missing --cov=../dashboard
```

You can also find the final report which has been added to the 'tests' directory as 'code_coverage.png'.

.. image:: .. image:: https://github.com/anish52/trade-analytics/blob/main/tests/code_coverage.png?sanitize=true

Contribute
----------
- Issue Tracker: https://github.com/anish52/trade-analytics/issues
- Source Code: https://github.com/anish52/trade-analytics

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: ankumar@ucsd.edu

License
-------

The project is licensed under the GNU license.
