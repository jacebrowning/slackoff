import log
from datafiles import datafile, field


@datafile
class Workspace:
    name: str
    active: bool = True


@datafile("~/Library/Preferences/slackoff.yml")
class Settings:
    workspaces: list[Workspace] = field(default_factory=list)

    def activate(self, name: str):
        log.debug(f"Marking workspace active: {name}")
        self._update(name, True)

    def deactivate(self, name: str):
        log.debug(f"Marking workspace inactive: {name}")
        self._update(name, False)

    def _update(self, name: str, active: bool):
        for workspace in self.workspaces:
            if workspace.name == name:
                workspace.active = active
                break
        else:
            self.workspaces.append(Workspace(name, active))


settings = Settings()
