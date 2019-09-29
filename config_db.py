from configparser import  ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in paramsL
        db[param[0]] = parm[1]
    else:
        raise  Exception(f'Secition {section} not found in the {filename} file')

    return db
