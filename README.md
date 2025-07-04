# hatch-build-freeze

### Hatch Dependency Freezing Plugin: Enhancing Build Consistency

Streamline your Python packaging workflow with this Hatch plugin designed to freeze your project's
dependency tree. By automatically resolving and pinning all direct and transitive dependencies into
a manifest file during the build process, it ensures:
* Reproducible Builds: Guarantee that your package builds with the same dependency versions every time.
* Consistent Environments: Simplify the creation of identical environments across development, testing, and production.
* Dependency Transparency: Provides a clear, version-locked list of all project dependencies.


## Configuration


### Calling the plugin

Modify `pyproject.toml` to include the plugin as a build dependency:

```toml
[build-system]
requires = ["hatchling", "hatch-build-freeze"]
build-backend = "hatchling.build"

[tool.hatch.build.hooks.hatch-build-freeze]
```

## Plugin Configuration


The following options are supported:

*   **`groups`** (optional, list of strings):
    Specifies a list of dependency groups (e.g., from `[dependency-groups]`) to include in the
    frozen requirements.
    ```toml
    [tool.hatch.build.hooks.hatch-build-freeze]
    groups = ["group1", "group2"]
    ```

*   **`extras`** (optional, list of strings):
    Specifies a list of optional dependency groups (e.g., from `[project.optional-dependencies]`)
    to include in the frozen requirements.
    ```toml
    [tool.hatch.build.hooks.hatch-build-freeze]
    extras = ["extra1", "extra2"]
    ```

*   **`uv-args`** (optional, list of strings):
    A list of additional command-line arguments to pass directly to the `uv export` command.
    ```toml
    [tool.hatch.build.hooks.hatch-build-freeze]
    uv-args = ["--resolution=lowest-direct", "--no-header"]
    ```
