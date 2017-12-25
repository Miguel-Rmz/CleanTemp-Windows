#!Python
"""
Deletes Windows %TEMP% and logs actions in specified log file
"""
__author__ = 'mramirez'

import sys, os
# adding Utilities holding directory to PYTHONPATH and importing it
sys.path.append(r'C:\Scripts\Python')
import Utilities.Common_Utils as CU

# cfg parameters
_LOGFILE = ''
_CLEANDIR = os.environ['temp']

# uses default log location %userprofile%\Reports\CleanTemp if _LOGFILE is null
if not _LOGFILE:
    _LOGFILE = CU.create_logDirs(os.path.join(os.environ['userprofile'], 'Reports/CleanTemp'), True, '%Y-%m-%d %H%M%S', 'CleanTempLog.log')
    
# executes cleanup and logs results
origNumDirs, origNumFiles = CU.get_num_dirs_files(_CLEANDIR)                # retrieves # of dirs and files before cleanup
CU.logger_datetime(_LOGFILE, 'STARTING CLEANUP: ' + _CLEANDIR)              # starts cleanup log                                      
for item in os.scandir(_CLEANDIR):                                          # creates iterator using os.scandir() and _CLEANDIR path
    CU.logger_datetime(_LOGFILE, CU.remove_dir_file(item, verbose=True))    # for item in iterator, attempt delete and log action
finalNumDirs, finalNumFiles = CU.get_num_dirs_files(_CLEANDIR)              # retrieves # of dirs and files after cleanup

# calculating deleted dirs/files
deletedDirs = origNumDirs - finalNumDirs ; errorDirs = origNumDirs - deletedDirs
deletedFiles = origNumFiles - finalNumFiles ; errorFiles = origNumFiles - deletedFiles

# continues and finishes logging
CU.logger_empty_line(_LOGFILE, 'Summary:\n')                                # starts summary log section
CU.logger(_LOGFILE, '-' * 26)
CU.logger(_LOGFILE, 'Dirs:   [{}] Attempted to delete: [{}] SUCCESS, [{}] ERROR'.format(origNumDirs, deletedDirs, errorDirs))
CU.logger(_LOGFILE, 'Files:  [{}] Attempted to delete: [{}] SUCCESS, [{}] ERROR'.format(origNumFiles, deletedFiles, errorFiles))
CU.logger_empty_line(_LOGFILE)
CU.logger_datetime(_LOGFILE, 'FINISHED CLEANUP: ' + _CLEANDIR)              # ends cleanup log
