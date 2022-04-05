on close()
    tell application "Google Chrome"
            close every tab of window 1 whose title is equal to "Login | Slack"
            close every tab of window 1 whose title is equal to "Redirecting… | Slack"
    end tell
end close
