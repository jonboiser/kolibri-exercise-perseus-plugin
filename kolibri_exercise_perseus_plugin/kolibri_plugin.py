from __future__ import absolute_import, print_function, unicode_literals

from kolibri.core.content import hooks as content_hooks
from kolibri.plugins.base import KolibriPluginBase


class ExercisePerseusRenderPlugin(KolibriPluginBase):
    pass


class ExercisePerseusRenderAsset(content_hooks.ContentRendererHook):
    unique_slug = "exercise_perseus_render_module"
    src_file = "assets/src/module.js"
    content_types_file = "content_types.json"
