@echo off


SET func=%1
SET prio=%2
SET text=%3
SET prio1="%2"
SET text1="%3"
shift

IF %func%x == x (
	python -c "import task; task.help()")

IF %func%x == helpx (
	python -c "import task; task.help()")
	
IF %func%x == addx ( IF %prio%x == x (echo Not Enough parameters in command. ) else ( IF %text%x == x (echo Not Enough parameters in command.) else ( python -c "import task; task.add("%prio1%","%text1%")")))
	
		
IF %func%x == lsx (
	python -c "import task; task.ls()")

IF %func%x == reportx (
	python -c "import task; task.report()")

IF %func%x == delx ( IF %prio%x == x (echo Not Enough parameters in command. ) else ( python -c "import task; task.delete("%prio1%")"))
	

IF %func%x == donex ( IF %prio%x == x (echo Not Enough parameters in command. ) else ( python -c "import task; task.done("%prio1%")"))

IF NOT %func%x == x ( IF NOT %func%x == helpx ( IF NOT %func%x == addx ( IF NOT %func%x == lsx ( IF NOT %func%x == reportx ( IF NOT %func%x == delx ( IF NOT %func%x == donex ( 
	echo Wrong Command. Please refer to help.
	python -c "import task; task.help()")))))))