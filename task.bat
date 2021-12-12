@echo off


SET func=%1
SET prio=%2
SET text=%3
shift

IF %func%x == x (
	python -c "import task; task.help()")

IF %func%x == helpx (
	python -c "import task; task.help()")
	
IF %func%x == addx (
	python -c "import task; task.add(%prio%,"%text%")")

IF %func%x == lsx (
	python -c "import task; task.ls()")

IF %func%x == reportx (
	python -c "import task; task.report()")

IF %func%x == delx (
	python -c "import task; task.delete(%prio%)")

IF %func%x == donex (
	python -c "import task; task.done(%prio%)")