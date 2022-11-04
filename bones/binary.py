import pickle
from os import remove


def Write_Binary_File(var, id):
    """
    Pass a variable of any type. And this function is able to save it in a file (binary), to be read later.
    """
    # if saved and file exists, delete to re-create updated
    try:
        remove("savingGOB"+str(id))
    except:
        pass

    # open('name_file', 'wb') w=write; b=binary
    file = open("savingGOB"+str(id), "wb")
    # save('variable', 'open_file')
    pickle.dump(var, file)
    # close file
    file.close
    print("\n\nGuardado Completado...\n\n")

def Read_Binary_File(id):
    """
    It is passed a (binary) file with instructions, and it reads it, and returns its instructions to be stored in a variable.
    """
    try:
        # open('name_file', 'rb') r=read; b=binary
        with open('savingGOB'+str(id), 'rb') as f:
            # read and charge file in variable
            var = pickle.load(f)

        print("\n\nCarga Completada...\n\n")
        # return variable with intruct
        return var

    except FileNotFoundError:
        print("\n\nError al Cargar, la partida no existe...\n\n")
        pass
