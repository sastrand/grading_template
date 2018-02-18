from os import environ, path, makedirs
from sys import argv
from string import Template
from argparse import ArgumentParser
import errno

def read_template():
    with open(TEMPLATE) as f:
        template = Template(f.read())
    f.close()
    return template

def read_student_list(student_list_path):
    with open(student_list_path) as f:
        student_list = f.read()
    f.close()
    return [s for s in student_list.split('\n') if s]

def gen_forms(template, gen_dirs):
    for s in student_list:
        if gen_dirs == True:
            dir_path = path.join(ASSGN_PATH, (s.replace(' ','_')))
            try:
                makedirs(dir_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            form_path = path.join(dir_path, (s.replace(' ','_')+".txt"))
            write_form(form_path, template.substitute(student_name=s))
        else:
            form_path = path.join(ASSGN_PATH, (s.replace(' ','_')+".txt"))
            write_form(form_path, template.substitute(student_name=s))

def write_form(form_path, form):
    with open(form_path, 'w') as f:
        f.write(form)
    f.close()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("assgn")
    parser.add_argument('-d', action="store_true")
    args = parser.parse_args()

    try: 
        ASSGN_PATH = path.join(environ["GRADING_PATH"], args.assgn)
        TEMPLATE = path.join(environ["GRADING_PATH"], args.assgn, "template.txt")
        student_list = read_student_list(environ["STUDENT_LIST"])
    except IndexError:
        print("""ERROR: You must include the name of the assignment in the 
                 template directory as argv[1].\nSee the README for help.""")
        exit(1)
    except KeyError:
        print("""ERROR: You must set the following two environment variables:
                 STUDENT_LIST the path to the class's student list and
                 GRADING_PATH the filename of the assignment in the template
                              directory.\nSee the README for help.""")
        exit(1)


    gen_forms(read_template(),args.d)
    print("Grading templates generated for {} students.\nWritten to {}".format(len(student_list), ASSGN_PATH))

