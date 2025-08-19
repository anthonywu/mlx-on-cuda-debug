This error happens if you run on a Linux with glibc < 2.35

The key error is `Wheels are available for `mlx` (v0.28.0) on the following platforms: `manylinux_2_35_x86_64`

```sh
$ modal run main.py::mlx_install_test
✓ Initialized. View run at https://modal.com/apps/anthonywu/main/ap-KrsrEZWV3A0VDXSeTMWwgQ
Building image im-6ILJxRuFV5CSTh5vZixvj9

Using legacy Image Builder version. We suggest upgrading at https://modal.com/settings/image-config.

=> Step 0: FROM base

=> Step 1: COPY --from=ghcr.io/astral-sh/uv:latest /uv /.uv/uv
Getting image source signatures
Copying blob sha256:e50e98c875f20bec2ac3f2cf0ac3e63da7982a0755cf21f7649795ea07ebd6f1
Copying blob sha256:070dd869fe4e79d0d7cea25367c07c65d820cc18988a353bd97aaadc7c472aac
Copying config sha256:7af8a183966208ab29078b00a3e00ddfb0ae2c28b4732945a5cab1d6970d25da
Writing manifest to image destination
Unpacking OCI image
   • unpacking rootfs ...
   • ... done
   • unpacked image rootfs: /tmp/.tmpmzKZQM

=> Step 2: RUN /.uv/uv pip install --python $(command -v python) --compile-bytecode mlx==0.28.0
Using Python 3.11.0 environment at: /usr/local
  × No solution found when resolving dependencies:
  ╰─▶ Because mlx==0.28.0 has no wheels with a matching platform tag (e.g.,
      `manylinux_2_31_x86_64`) and you require mlx==0.28.0, we can conclude
      that your requirements are unsatisfiable.

      hint: Wheels are available for `mlx` (v0.28.0) on the following
      platforms: `manylinux_2_35_x86_64`, `macosx_13_0_arm64`,
      `macosx_14_0_arm64`, `macosx_15_0_arm64`
Terminating task due to error: failed to run builder command "/.uv/uv pip install --python $(command -v python) --compile-bytecode mlx==0.28.0": container exit status: 1
Runner failed with exit code: -1
Stopping app - uncaught exception raised locally: RemoteError('Image build for im-6ILJxRuFV5CSTh5vZixvj9 failed. See build logs for more details.').
╭─ Error ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Image build for im-6ILJxRuFV5CSTh5vZixvj9 failed. See build logs for more details.                                                                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
