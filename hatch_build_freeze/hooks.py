# Copyright 2025 Minds.ai, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Hooks for Hatch build freeze."""

from hatchling.plugin import hookimpl

from hatch_build_freeze.plugin import HatchBuildFreezePlugin


@hookimpl
def hatch_register_build_hook() -> type[HatchBuildFreezePlugin]:
    """Register the build hook for Hatch Build Freeze."""
    return HatchBuildFreezePlugin
