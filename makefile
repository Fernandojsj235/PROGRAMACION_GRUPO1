venv/bin/activate: requirements.txt
	python -m venv venv
	./venv/bin/pip install -r requirements.txt

run:venv/bin/activate
	./venv/bin/streamlit run app.py		
