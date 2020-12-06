#!/bin/bash

osascript - "$@" <<END 1>/dev/null
	on run argv
		tell application "Notes"
			activate
			set n to item 1 of argv as string
			tell account "iCloud"
				tell folder "Youtube"
					make new note with properties {name:n}
				end tell
			end tell
		end tell
	end run
END
