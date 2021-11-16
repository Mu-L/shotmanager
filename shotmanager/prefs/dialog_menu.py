# GPLv3 License
#
# Copyright (C) 2021 Ubisoft
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
-
"""

import bpy
from bpy.types import Menu

from shotmanager.config import config


class UAS_MT_ShotManager_Prefs_MainMenu(Menu):
    bl_idname = "UAS_MT_Shot_Manager_prefs_mainmenu"
    bl_label = "Settings for the Shot Manager instanced in this scene"
    # bl_description = "Display the settings for the Shot Manager instanced in the current scene"

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.operator_context = "INVOKE_DEFAULT"
        row.operator("shot_manager.features", text="Features...")

        layout.separator()

        row = layout.row(align=True)
        row.operator("uas_shot_manager.project_settings_prefs", text="Project Settings...")
        row = layout.row(align=True)
        row.operator("uas_shot_manager.general_prefs", text="Scene Settings...")
        row = layout.row(align=True)
        row.operator("uas_shot_manager.sequence_prefs", text="Sequence Settings...")

        layout.separator()

        row = layout.row(align=True)
        row.operator_context = "INVOKE_DEFAULT"
        row.operator("uas_shot_manager.shots_prefs", text="Shots Display...")  # , icon="SETTINGS")

        layout.separator()

        # row = layout.row(align=True)
        # row.operator_context = "INVOKE_DEFAULT"
        # row.operator("uas_shot_manager.tools_prefs", text="Tools Settings...")

        row = layout.row(align=True)
        row.operator_context = "INVOKE_DEFAULT"
        row.operator("uas_shot_manager.overlay_tools_prefs", text="Overlay Tools Settings...")

        layout.separator()

        row = layout.row(align=True)
        row.operator("preferences.addon_show", text="Add-on Preferences...").module = "shotmanager"

        if config.devDebug:
            layout.separator()
            row = layout.row(align=True)
            row.label(text="Tools for Debug:")

            row = layout.row(align=True)
            row.operator_context = "INVOKE_DEFAULT"
            row.label(text="Add debug operator here")
            # row.operator("uas_shot_manager.predec_shots_from_single_cam")

        layout.separator()
        row = layout.row(align=True)

        row = layout.row(align=True)
        row.operator_context = "INVOKE_DEFAULT"
        row.operator("uas_shot_manager.file_info", text="File Info...")

        layout.separator()

        row = layout.row(align=True)
        doc_op = row.operator("shotmanager.open_documentation_url", text="Documentation")
        doc_op.path = "https://ubisoft-shotmanager.readthedocs.io"
        doc_op.tooltip = "Open online documentation: " + doc_op.path

        layout.separator()

        row = layout.row(align=True)
        row.operator("uas_shot_manager.about", text="About...")


_classes = (UAS_MT_ShotManager_Prefs_MainMenu,)


def register():
    for cls in _classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
