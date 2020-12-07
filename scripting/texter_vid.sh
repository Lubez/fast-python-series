#!/bin/bash

# bash texter_vid.sh {number} {message}
osascript - "$@" <<END 1>/dev/null
	tell application "Messages"
		activate
		set targetService to 1st service whose service type = iMessage
		set targetBuddy to buddy "$1" of targetService
		send "$2" to targetBuddy
	end tell
END