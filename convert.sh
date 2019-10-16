find . -name "*.ui" -exec sh -c 'pyside2-uic $0 > converted/$(basename $0 .ui).py' {} \;
