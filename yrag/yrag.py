import sys
import os

loc,*arg =sys.argv

if arg[0] in ["-h","--help"]:
    print("""
    -----------------------------------------------------------
    Welcome to use YRAG !
    This is a framework to build up and deploy AI model quickly.
    So far, we have several functional command below.
    Please refer descriptions and Have a joyful experience!      
    ------------------------------------------------------------
    yrag build <project name> - Build up a application with the name up to you.
    yrag deploy - Deploy this app in specific docker server.  
    """)
elif arg[0]=="build":
    path_cwd = os.getcwd()
    print(arg[1])
