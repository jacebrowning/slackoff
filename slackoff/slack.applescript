on activate()
	tell application "Slack" to activate
	tell application "System Events"
		tell its process "Slack"
			click menu bar item "Slack" of menu bar 1
		end tell
	end tell
end activate

on signin(workspace)
	tell application "System Events"
		tell its process "Slack"
			click menu item "Sign in to Another Workspace…" of menu 1 of menu item "Workspace" of menu 1 of menu bar item "File" of menu bar 1
		end tell
	end tell
    delay 2
    tell application "Google Chrome"
	    tell active tab of front window
		    execute javascript "document.evaluate('//div[text()=\"" & workspace & "\"]', document).iterateNext().click()"
            delay 1
            execute javascript "document.evaluate('//button[text()=\"Open\"]', document).iterateNext().click()"
        end tell
	end tell
end signin

on signout(workspace)
	tell application "System Events"
		tell its process "Slack"
			click menu item workspace of menu 1 of menu item "Sign Out" of menu 1 of menu bar item "Slack" of menu bar 1
		end tell
	end tell
end signout
