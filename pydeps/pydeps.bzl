"Public API for interacting with the pydeps rule/aspect."

load("//pydeps/private/enforcer:enforcer.bzl", _deps_enforcer_aspect_factory = "deps_enforcer_aspect_factory")
load("//pydeps/private/index:deps_index.bzl", _deps_index = "deps_index")

pip_deps_index = _deps_index

deps_enforcer_aspect_factory = _deps_enforcer_aspect_factory
