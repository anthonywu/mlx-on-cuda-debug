This error happens if you run on a machine without a GPU device.

```sh
$ modal run main.py::ldd_version_latest_debian_slim
✓ Initialized. View run at https://modal.com/apps/anthonywu/main/ap-VmB22vlJY081iLi8Z3VUuK
✓ Created objects.
├── 🔨 Created mount /Users/anthonywu/workspace/mlx-on-cuda/modal/main.py
├── 🔨 Created function ldd_version_latest_debian_slim.
└── 🔨 Created function ldd_version_default_modal_debian_slim.
ldd (Debian GLIBC 2.41-12) 2.41
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Written by Roland McGrath and Ulrich Drepper.

Stopping app - local entrypoint completed.
✓ App completed. View run at https://modal.com/apps/anthonywu/main/ap-VmB22vlJY081iLi8Z3VUuK
(mlx-on-cuda)  anthonywu@lunar-shadow  ~/Desktop/workspace/mlx-on-cuda/modal   main  modal run main.py::mlx_quick_test
✓ Initialized. View run at https://modal.com/apps/anthonywu/main/ap-WfN0cnOffgjjaYs8ZrcAwi
Building image im-qdMWzBVsSgbCzdaYECkYJA

Using legacy Image Builder version. We suggest upgrading at https://modal.com/settings/image-config.

=> Step 0: FROM base

=> Step 1: COPY --from=ghcr.io/astral-sh/uv:latest /uv /.uv/uv
Getting image source signatures
Copying blob sha256:070dd869fe4e79d0d7cea25367c07c65d820cc18988a353bd97aaadc7c472aac
Copying blob sha256:e50e98c875f20bec2ac3f2cf0ac3e63da7982a0755cf21f7649795ea07ebd6f1
Copying config sha256:7af8a183966208ab29078b00a3e00ddfb0ae2c28b4732945a5cab1d6970d25da
Writing manifest to image destination
Unpacking OCI image
   • unpacking rootfs ...
   • ... done
   • unpacked image rootfs: /tmp/.tmpsaErdJ

=> Step 2: RUN /.uv/uv pip install --python $(command -v python) --compile-bytecode mlx==0.28.0 'mlx[cuda]==0.28.0'
Using Python 3.11.5 environment at: /usr/local
Resolved 5 packages in 165ms
Downloading nvidia-cudnn-cu12 (545.2MiB)
Downloading nvidia-cublas-cu12 (554.3MiB)
Downloading nvidia-cuda-nvrtc-cu12 (85.4MiB)
Downloading mlx-cuda (46.0MiB)
 Downloading nvidia-cuda-nvrtc-cu12
 Downloading nvidia-cudnn-cu12
 Downloading nvidia-cublas-cu12
 Downloading mlx-cuda
Prepared 5 packages in 11.01s
Installed 5 packages in 147ms
Bytecode compiled 2578 files in 3.01s
 + mlx==0.28.0
 + mlx-cuda==0.28.0
 + nvidia-cublas-cu12==12.9.1.4
 + nvidia-cuda-nvrtc-cu12==12.9.86
 + nvidia-cudnn-cu12==9.12.0.46
Saving image...
Image saved, took 5.47s

Built image im-qdMWzBVsSgbCzdaYECkYJA in 25.18s


✓ Created objects.
├── 🔨 Created mount /Users/anthonywu/workspace/mlx-on-cuda/modal/main.py
├── 🔨 Created function ldd_version_latest_debian_slim.
├── 🔨 Created function ldd_version_default_modal_debian_slim.
└── 🔨 Created function mlx_quick_test.
Traceback (most recent call last):
  File "/pkg/modal/_runtime/container_io_manager.py", line 778, in handle_input_exception
    yield
  File "/pkg/modal/_container_entrypoint.py", line 243, in run_input_sync
    res = io_context.call_finalized_function()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/pkg/modal/_runtime/container_io_manager.py", line 197, in call_finalized_function
    res = self.finalized_function.callable(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/main.py", line 46, in mlx_quick_test
    import mlx.core as mx
ImportError: libcuda.so.1: cannot open shared object file: No such file or directory
Stopping app - uncaught exception raised in remote container: ImportError('libcuda.so.1: cannot open shared object file: No such file or directory').
╭─ Error ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ libcuda.so.1: cannot open shared object file: No such file or directory                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
