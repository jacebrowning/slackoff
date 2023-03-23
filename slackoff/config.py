from dataclasses import dataclass

import log
from datafiles import datafile, field


@dataclass
class Workspace:
    name: str
    active: bool = True
    uses: int = 0


@datafile("~/Library/Preferences/slackoff.yml")
@dataclass
class Settings:
    workspaces: list[Workspace] = field(default_factory=list)

    def activate(self, name: str):
        log.debug(f"Marking workspace active: {name}")
        workspace = self._update(name, True)
        workspace.uses += 1

    def deactivate(self, name: str):
        log.debug(f"Marking workspace inactive: {name}")
        self._update(name, False)

    def _update(self, name: str, active: bool):
        for workspace in self.workspaces:
            if workspace.name == name:
                workspace.active = active
                return workspace

        workspace = Workspace(name, active)
        self.workspaces.append(workspace)
        return workspace


settings = Settings()
