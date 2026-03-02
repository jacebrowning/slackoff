from dataclasses import dataclass

import log
from datafiles import datafile, field

PATH = "~/Library/Preferences/slackoff.yml"


@dataclass
class Workspace:
    name: str
    profile: str = ""
    active: bool = True
    uses: int = 0


@datafile(PATH)
@dataclass
class Settings:
    workspaces: list[Workspace] = field(default_factory=list)

    def activate(self, name: str, profile: str | None = None):
        log.debug(f"Marking workspace active: {name}")
        workspace = self._update(name, True, profile)
        workspace.uses += 1

    def deactivate(self, name: str):
        log.debug(f"Marking workspace inactive: {name}")
        self._update(name, False)

    def get_profile(self, name: str) -> str | None:
        for workspace in self.workspaces:
            if workspace.name == name and workspace.profile:
                return workspace.profile
        return None

    def _update(self, name: str, active: bool, profile: str | None = None):
        for workspace in self.workspaces:
            if workspace.name == name:
                workspace.active = active
                if profile is not None:
                    workspace.profile = profile
                return workspace

        workspace = Workspace(name, profile or "", active, 0)
        self.workspaces.append(workspace)
        return workspace


settings = Settings()
