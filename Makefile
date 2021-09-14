win: venv-init activate	
	pip3 install deps/win/PyOpenGL_accelerate-3.1.5-cp39-cp39-win_amd64.whl
	pip3 install deps/win/PyOpenGL-3.1.5-cp39-cp39-win_amd64.whl

unix: venv-init activate
	pip3 install PyOpenGL==3.1.5

venv-init:
	python -m venv venv

activate:
	source venv/Scripts/activate

deactivate:
	deactivate
