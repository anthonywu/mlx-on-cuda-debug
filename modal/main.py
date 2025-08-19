import modal

app = modal.App("mlx-on-cuda")


# ==== debian_slim as shown on Modal tutorials =====
basic_image = modal.Image.debian_slim(python_version="3.11")
"""
ldd --version would return:
    ldd (Debian GLIBC 2.31-13+deb11u5) 2.31
"""


# ==== debian:stable-20250811-slim =====

"""
ldd --version would return:
    ldd (Debian GLIBC 2.41-12) 2.41
"""
latest_debian_slim = modal.Image.from_registry(
    "debian:stable-20250811-slim", add_python="3.11"
)


mlx_on_cuda_image = modal.Image.from_registry(
    "debian:stable-20250811-slim", add_python="3.11"
).uv_pip_install("mlx==0.28.0", "mlx[cuda]==0.28.0")


@app.function(image=basic_image)
def ldd_version_default_modal_debian_slim():
    import subprocess

    result = subprocess.run(["ldd", "--version"], capture_output=True, text=True)
    print(result.stdout)


@app.function(image=latest_debian_slim)
def ldd_version_latest_debian_slim():
    import subprocess

    result = subprocess.run(["ldd", "--version"], capture_output=True, text=True)
    print(result.stdout)


# the `mlx[cuda]` package only installs on a recent image such as debian:stable-20250811-slim
# run this function with: 'modal run main.py::mlx_quick_test'
@app.function(image=mlx_on_cuda_image, gpu="A100")
def mlx_quick_test():
    import subprocess

    print(subprocess.run(["ldd", "--version"], capture_output=True, text=True).stdout)
    print(
        subprocess.run(
            ["python", "-m", "pip", "freeze"], capture_output=True, text=True
        ).stdout
    )
    try:
        import mlx.core as mx
    except ImportError:
        # if this happens, need to run on gpu
        return False

    # mx.set_default_device(mx.gpu)  # if we have to set this
    print(f"{mx.default_device()=}")
    a = mx.array([1, 2, 3])
    b = mx.array([4, 5, 6])

    c = a + b
    mx.eval(c)
    print(c)
    return True


def foo():
    with modal.enable_output():
        with app.run():
            mlx_quick_test.remote()
