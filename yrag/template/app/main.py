from importlib import import_module
from fastapi import FastAPI
import os

app = FastAPI(title="MY AWESOME MODEL")
files_name = os.listdir("./app/models")
modules=[f[:-3] for f in files_name if f[:5]=="model" and f[-3:]==".py"]
for module_name in modules :
    module = import_module(f"app.models.{module_name}")
    f = getattr(module,module_name)
    app.post(f"/{module_name[6:]}")(f)

