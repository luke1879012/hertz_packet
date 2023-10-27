参考1 :
https://cloud.tencent.com/developer/beta/article/1757852




相关指令：
```shell
python setup.py sdist build
twine upload dist/*
```

参考2 :
https://cloud.tencent.com/developer/article/2219745

指令:
```shell
python -m pip install --upgrade build
python -m build
twine upload dist/*
```
