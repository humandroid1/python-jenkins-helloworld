import sys
import datetime
import pip
import pkg_resources
built_in_mod = sys.modules
#print(built_in_mod.keys())
'''if "sys" in built_in_mod:
    print("true")'''
#a=[datetime]
#res=set(a)-set(built_in_mod)
#print(list(res))
print(built_in_mod.keys())
print("***************")
pkgs = []
pkgs1=[]
#print([pip.main(['list'])])
installed = [pkg.key for pkg in pkg_resources.working_set]
print(installed)
print("****************")
with open('C:\Users\user\PycharmProjects\pyprojects\checkpymod.py') as f:
    for lines in f:
        if "import" in lines and "#" not in lines:
            tmp = lines.split("import")
            #print(tmp[-1])
            #if tmp[-1].strip() not in built_in_mod and (tmp[-1].strip() not in installed or (tmp[-1].strip()).lower() not in installed):
            if tmp[-1].strip() not in built_in_mod and (tmp[-1].strip()).lower() not in installed:
            #if tmp[-1].strip() not in built_in_mod:
                    pkgs.append((tmp[-1].strip()))

if len(pkgs) is not 0:
    print(pkgs)
    #pip.main(['install'] + pkgs)
    print("******************")
else:
    print("All the Packages are installed...You are Good to go...")
#pkgs = set(pkgs)-set(installed)
#print(list(pkgs))
#for package in pkgs:
'''if package in installed or package.lower() in installed:
            set(pkgs)-package
            print(list(pkgs))'''
