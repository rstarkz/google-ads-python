# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v14.enums",
    marshal="google.ads.googleads.v14",
    manifest={
        "DataDrivenModelStatusEnum",
    },
)


class DataDrivenModelStatusEnum(proto.Message):
    r"""Container for enum indicating data driven model status."""

    class DataDrivenModelStatus(proto.Enum):
        r"""Enumerates data driven model statuses."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        AVAILABLE = 2
        STALE = 3
        EXPIRED = 4
        NEVER_GENERATED = 5


__all__ = tuple(sorted(__protobuf__.manifest))
