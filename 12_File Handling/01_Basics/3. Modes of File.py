# python provides several modes for file operations that control how files are opened and what operations are permitted. Here's the complete list:

# 1. Basic Modes

Mode   Description	     File Position	  If File Exists	If File Doesn't Exist
'r'	    Read (default)   	Start	        Opens	Raises FileNotFoundError
'w'	    Write	            Start	        Truncates	Creates new
'a'	    Append	            End	Preserves content	Creates new
'x'	    Exclusive creation	Start	Raises FileExistsError	Creates new