Environment Setup and user guide:

1. In PyCharm, go to File > Settings > Project: prezentTestProject > Python Interpreter.
2. Click Add Interpreter > Add New Environment > Virtualenv.
3. Specify the folder (venv) and create the environment.
4. In Pycharm select the prezentProject > PyCahrm > Settings
	a. Tools> Python Integrated Tools > Testing > Select Default test runner Pytest
		Click Apply
	b. Terminal > Application Settings > Select Activate virtualenv
		Click Apply
		Click Ok

5. Restart Pycharm

7. Create requirements.txt under prezentProject with following modules entry:

	selenium>=4.0.0
	pytest
	pytest-html

6. Install Dependencies: Open the terminal in PyCharm and run:

	pip install -r requirements.txt

7. Check all of the desired modules installed
	pip list

	Following should appear
	(venv) gargisingh@Gargis-MacBook-Pro prezentProject % pip list
		Package            Version
		------------------ -----------
		anyio              4.6.2.post1
		attrs              24.2.0
		certifi            2024.6.2
		charset-normalizer 3.3.2
		decorator          5.1.1
		greenlet           3.0.3
		h11                0.14.0
		idna               3.7
		iniconfig          2.0.0
		Jinja2             3.1.4
		MarkupSafe         3.0.2
		outcome            1.3.0.post0
		packaging          24.1
		pip                24.3.1
		playwright         1.44.0
		pluggy             1.5.0
		pyee               11.1.0
		PySocks            1.7.1
		pytest             8.2.2
		pytest-asyncio     0.24.0
		pytest-base-url    2.1.0
		pytest-html        4.1.1
		pytest-metadata    3.1.1
		pytest-playwright  0.5.0
		pytest-tornasync   0.6.0.post2
		pytest-trio        0.8.0
		python-slugify     8.0.4
		requests           2.32.3
		selenium           4.26.1
		sniffio            1.3.1
		sortedcontainers   2.4.0
		text-unidecode     1.3
		tornado            6.4.1
		trio               0.27.0
		trio-websocket     0.11.1
		typing_extensions  4.12.2
		urllib3            2.2.1
		websocket-client   1.8.0
		wsproto            1.2.0


8. Start working in Folder structure
			prezentTestProject/
			│
			├── pages/
			│   ├── __init__.py
			│   ├── base_page.py
   			│   ├── fingerprint_page.py
			│   ├── login_page.py
			│   ├── profile_page.py
			│   ├── templates_page.py
			│
			├── tests/
			│   ├── __init__.py
			│   ├── base_test.py
			│   ├── test_login_profile.py
			│   ├── test_finger_print.py
			│
			├── venv/                 # Virtual environment folder (created via PyCharm or manually)
			│
			├── conftest.py
			├── requirements.txt
			├── pytest.ini            # configuration for pytest
			├── README.md             

   
10. Run Tests:
	pytest --browser=chrome

11. Git Configuration
    In terminal go to project directory
        git init
        git add .
        git commit -m "Initial commit for Selenium Base POM Framework"
        git remote add origin https://github.com/qasudershan/POMSample.git
        git branch -M master 
        git push -u origin master
