from datafiles import datafile, field


@datafile("~/Library/Preferences/slackoff.yml")
class Settings:
    workspaces: list[str] = field(default_factory=list)


settings = Settings()
