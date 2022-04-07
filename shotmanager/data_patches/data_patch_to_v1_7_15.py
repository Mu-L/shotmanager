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
Data patch
"""

import bpy
from ..utils import utils

from ..config import sm_logging

_logger = sm_logging.getLogger(__name__)

# 06/04/2022
# Patch to upgrade the shot manager data created with a shot manager version older than V.1.7.15

# v1_7_15: 1007015


def data_patch_to_v1_7_15():
    """Patch to introduce the new project naming identifiers of the properties"""
    _logger.debug_ext(f"Applying patch {'data_patch_to_v1_7_15'}...", col="PINK", tag="PATCH")

    for scene in bpy.data.scenes:
        props = None

        if getattr(scene, "UAS_shot_manager_props", None) is not None:
            props = scene.UAS_shot_manager_props

            _logger.debug_ext(
                f"   Data version: {props.dataVersion}, SM version: {bpy.context.window_manager.UAS_shot_manager_version}"
            )
            if props.dataVersion <= 0 or props.dataVersion < bpy.context.window_manager.UAS_shot_manager_version:

                # apply patch and apply new data version
                #       print("       Applying data patch data_patch_to_v1_7_15 to scenes")

                props.project_naming_project_format = "Act##"
                props.project_naming_sequence_format = "Seq####"
                props.project_naming_shot_format = "Sh####"
                props.project_naming_separator_char = "_"
                props.project_naming_project_index = -1
                props.project_naming_sequence_index = -1

                # check issue found on some old scenes
                if (
                    "Render Settings" == props.renderSettingsStill.name
                    or "Render Settings" == props.renderSettingsAnim.name
                    or "Render Settings" == props.renderSettingsAll.name
                    or "Render Settings" == props.renderSettingsOtio.name
                    or "Render Settings" == props.renderSettingsPlayblast.name
                ):
                    props.reset_render_properties()

                # set right data version
                # props.dataVersion = bpy.context.window_manager.UAS_shot_manager_version
                props.dataVersion = bpy.context.window_manager.UAS_shot_manager_version
                print(
                    f"       Scene {scene.name}: Data upgraded to version V.{utils.convertVersionIntToStr(props.dataVersion)}"
                )
