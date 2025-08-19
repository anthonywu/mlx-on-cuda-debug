`mlx[cuda]`'s requirements as documented upstream is:

- Nvidia architecture >= SM 7.0 (Volta)
- Nvidia driver >= 550.54.14
- CUDA toolkit >= 12.0
- Linux distribution with glibc >= 2.35
- Python >= 3.9

The following setup meets all requirements, the error happens on:

- `debian:stable-20250811-slim`
- `Debian GLIBC 2.41-12` (satisfies `glibc>2.35` requirement for built `mlx[cuda]` wheels)
- Nvidia `Driver Version: 575.57.08`
- `CUDA Version: 12.9`
- `NVIDIA A100-SXM4-40GB, 8.0`
- Python 3.11


```py
# env setup on modal
mlx_on_cuda_image = modal.Image.from_registry(
    "debian:stable-20250811-slim", add_python="3.11"
).uv_pip_install("mlx==0.28.0", "mlx[cuda]==0.28.0")
```

```sh
$ modal run main.py::mlx_quick_test
✓ Initialized. View run at https://modal.com/apps/anthonywu/main/ap-yjnFOD1ifwN1yshIuohRf8
✓ Created objects.
├── 🔨 Created mount /Users/anthonywu/workspace/mlx-on-cuda/modal/main.py
├── 🔨 Created function ldd_version_default_modal_debian_slim.
├── 🔨 Created function ldd_version_latest_debian_slim.
└── 🔨 Created function mlx_quick_test.
Tue Aug 19 23:54:22 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 575.57.08              Driver Version: 575.57.08      CUDA Version: 12.9     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-SXM4-40GB          On  |   00000000:80:00.0 Off |                    0 |
| N/A   36C    P0             52W /  400W |       0MiB /  40960MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

NVIDIA A100-SXM4-40GB, 8.0

ldd (Debian GLIBC 2.41-12) 2.41
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Written by Roland McGrath and Ulrich Drepper.

aiohttp==3.8.3
aiosignal==1.4.0
aiostream==0.4.4
anyio==4.10.0
asgiref==3.5.2
asttokens==3.0.0
async-timeout==4.0.3
attrs==25.3.0
certifi==2025.8.3
charset-normalizer==2.1.1
click==8.2.1
cloudpickle==2.2.0
commonmark==0.9.1
decorator==5.2.1
executing==2.2.0
fastapi==0.88.0
fastprogress==1.0.0
frozenlist==1.7.0
grpclib==0.4.3
h2==4.2.0
hpack==4.1.0
hyperframe==6.1.0
idna==3.10
importlib-metadata==4.8.1
ipython==9.4.0
ipython_pygments_lexers==1.1.1
jedi==0.19.2
matplotlib-inline==0.1.7
mlx==0.28.0
mlx-cuda==0.28.0
multidict==6.6.4
numpy==2.3.2
nvidia-cublas-cu12==12.9.1.4
nvidia-cuda-nvrtc-cu12==12.9.86
nvidia-cudnn-cu12==9.12.0.46
parso==0.8.4
pexpect==4.9.0
prompt_toolkit==3.0.51
propcache==0.3.2
protobuf==6.32.0
ptyprocess==0.7.0
pure_eval==0.2.3
pydantic==1.10.22
Pygments==2.19.2
python-multipart==0.0.20
rich==12.3.0
sniffio==1.3.1
stack-data==0.6.3
starlette==0.22.0
tblib==1.7.0
toml==0.10.2
traitlets==5.14.3
typeguard==4.4.4
typer==0.6.1
types-certifi==2021.10.8.3
types-toml==0.10.4
typing_extensions==4.14.1
wcwidth==0.2.13
yarl==1.20.1
zipp==3.23.0

Stopping app - local entrypoint completed.
Exception ignored in atexit callback: <nanobind.nb_func object at 0x2ac5e7999360>
RuntimeError: cudaMemAdvise(data_, small_pool_size, cudaMemAdviseSetReadMostly, 0) failed: invalid argument
✓ App completed. View run at https://modal.com/apps/anthonywu/main/ap-dolgG8hdv4BiLURQuX1WKQ
```
