generate_resources:
	pyrcc5 -compress 9 app/resources/resources.qrc -o app/resources/resources.py

generate_ui: generate_resources
	pyuic5 app/ui_files/main_window.ui --import-from=app.resources -o app/gui/window.py --resource-suffix=
	pyuic5 app/ui_files/w1.ui -o app/gui/widget1.py
	pyuic5 app/ui_files/w2.ui -o app/gui/widget2.py
	pyuic5 app/ui_files/w3.ui --import-from=app.resources -o app/gui/widget3.py --resource-suffix=

.PHONY: build
build:
	pyinstaller -F -w runapp.py