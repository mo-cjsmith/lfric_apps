import sys

from metomi.rose.upgrade import MacroUpgrade  # noqa: F401

from .version31_32 import *


class UpgradeError(Exception):
    """Exception created when an upgrade fails."""

    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        sys.tracebacklimit = 0
        return self.msg

    __str__ = __repr__


class vn32_t763(MacroUpgrade):
    """Upgrade macro for PR #763 by Chris Smith."""

    BEFORE_TAG = "vn3.2"
    AFTER_TAG = "vn3.2_t763"

    def upgrade(self, config, meta_config=None):
        """Add new wind_relax namelist"""
        source = self.get_setting_value(
            config, ["file:configuration.nml", "source"])
        source = source + "\n" + " (namelist:wind_relax)"
        self.change_setting_value(
            config, ["file:configuration.nml", "source"], source)
        """Add wind_relaxation setting to external_forcing namelist"""
        self.add_setting(
            config, ["namelist:external_forcing", "wind_relaxation"], ".false.")
        """Data for wind_relax namelist"""
        self.add_setting(config, ["namelist:wind_relax"])
        self.add_setting(
            config, ["namelist:wind_relax", "coordinate"], "'height'")
        self.add_setting(config, ["namelist:wind_relax", "heights"], "0.0")
        self.add_setting(
            config, ["namelist:wind_relax", "number_heights"], "1")
        self.add_setting(config, ["namelist:wind_relax", "number_times"], "1")
        self.add_setting(config, ["namelist:wind_relax", "times"], "0.0")
        self.add_setting(config, ["namelist:wind_relax", "timescale"], "1.0")
        self.add_setting(
            config, ["namelist:wind_relax", "u_profile_data"], "0.0")
        self.add_setting(
            config, ["namelist:wind_relax", "v_profile_data"], "0.0")
        return config, self.reports
