import sys
import os
import shutil

def main():
    directory_path = os.path.dirname(os.path.abspath(__file__))
    loc,*arg =sys.argv
    if len(arg)==0:
        arg.append("-h")
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
        print("Yrag is Building ... ")
        src = os.path.join(directory_path,"template")
        dist = os.path.join(os.getcwd(),"build")
        if os.path.isdir(dist):
            shutil.rmtree(dist)
        shutil.copytree(src,dist)

        model_src = os.path.join(os.getcwd(),"models")
        model_dist = os.path.join(os.getcwd(),"build","app","models")
        shutil.copytree(model_src,model_dist)
        print("Build id done.")
        
        
    elif arg[0]=="run":
        print("Choose a good name for your image:\n")
        image = input("Choose a good name for your image:\n")
        container = input("Choose a good name for your container:\n")
        port = input("Choose a port:\n")
        os.system(f"docker rm -f {container}")
        os.system(f"docker build -f ./build/Dockerfile -t {image} .")
        os.system(f"docker run -d --name {container} -p {port}:80 {image}")

if __name__ == "__main__":
    main()
