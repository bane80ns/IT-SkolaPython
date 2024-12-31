import platform

print(platform.system(), platform.platform(), platform.machine())

# Verzija pythona na mom racunaru je
py_ver = platform.python_version()
py_ver_singledigit = int(platform.python_version_tuple()[0])
print(py_ver_singledigit)
print(py_ver)

print(f"Verzija Python-a na mom racunaru je: {py_ver}")

# Ako je verzija python-a koju koristimo veca ili manja od 3, onda ispisati poruku "ne koristite dobru verziju pytona-"

if py_ver_singledigit != 3:
    print("Ne koristite dobru verziju Python-a")
else:
    print("Imate dobru verziju pyton-a")
