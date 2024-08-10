## Python module import and execution

* The python interpreter assigns `__name__` to each module at runtime (when module is imported)
* `__name__` is set as `__main__` if the module is directly called from python
* on module import, the code for that module is run (else condition in `add` and `multiply`) 