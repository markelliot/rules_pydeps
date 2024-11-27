"define aspects"

load("@rules_pydeps//pydeps:pydeps.bzl", "deps_enforcer_aspect_factory")

deps_enforcer = deps_enforcer_aspect_factory(
    pip_deps_index = Label("@reqs//:pip_deps_index"),
)
