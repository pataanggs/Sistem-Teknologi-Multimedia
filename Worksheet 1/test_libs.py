import importlib

# Daftar library dari requirements.txt
libraries = [
    "anyio", "argon2", "arrow", "asttokens", "async_lru", "attrs", "audioread",
    "babel", "bs4", "bleach", "certifi", "cffi", "charset_normalizer", "colorama",
    "comm", "contourpy", "cycler", "debugpy", "decorator", "defusedxml", "exceptiongroup",
    "executing", "fastjsonschema", "fonttools", "fqdn", "h11", "httpcore", "httpx",
    "idna", "imageio", "imageio_ffmpeg", "ipykernel", "IPython", "ipywidgets",
    "isoduration", "jedi", "jinja2", "joblib", "json5", "jsonpointer", "jsonschema",
    "jupyter", "jupyter_client", "jupyter_console", "jupyter_core", "jupyter_events",
    "jupyter_lsp", "jupyter_server", "jupyter_server_terminals", "jupyterlab",
    "jupyterlab_pygments", "jupyterlab_server", "jupyterlab_widgets", "kiwisolver",
    "lark", "lazy_loader", "librosa", "llvmlite", "markupsafe", "matplotlib",
    "matplotlib_inline", "mistune", "moviepy", "msgpack", "nbclient", "nbconvert",
    "nbformat", "nest_asyncio", "networkx", "notebook", "notebook_shim", "numba",
    "numpy", "cv2", "overrides", "packaging", "pandas", "pandocfilters", "parso",
    "PIL", "platformdirs", "pooch", "proglog", "prometheus_client", "prompt_toolkit",
    "psutil", "pure_eval", "pycparser", "pygments", "pyparsing", "dateutil",
    "dotenv", "python_json_logger", "pytz", "pywin32", "pywinpty", "yaml", "zmq",
    "referencing", "requests", "rfc3339_validator", "rfc3986_validator",
    "rfc3987_syntax", "rpds", "skimage", "sklearn", "scipy", "send2trash",
    "setuptools", "six", "sniffio", "soundfile", "soupsieve", "soxr", "stack_data",
    "terminado", "threadpoolctl", "tifffile", "tinycss2", "tomli", "tornado",
    "tqdm", "traitlets", "types_python_dateutil", "typing_extensions", "tzdata",
    "uri_template", "urllib3", "wcwidth", "webcolors", "webencodings",
    "websocket", "widgetsnbextension"
]

failed = []

print("🔍 Testing installed libraries...\n")

for lib in libraries:
    try:
        importlib.import_module(lib)
        print(f"✅ {lib} imported successfully")
    except Exception as e:
        print(f"❌ {lib} failed -> {e}")
        failed.append(lib)

print("\n=== SUMMARY ===")
if not failed:
    print("🎉 All libraries imported successfully!")
else:
    print(f"⚠️ Failed to import {len(failed)} libraries: {failed}")
