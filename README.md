## Grading Template Generator

This tool will read a template text file with a student name field marked with
`${student_name}` and a new-line separated list of student and generate a template
for each student.

With the optional directory flag, the program will generate a directory for each
student and place their feedback template inside of it.

### Running the Program

The program uses the following environment variables:
    * `GRADING_PATH` This is the path to a directory containing all feedback templates for a given term or class. 
    * `STUDENT_LIST` This is the full path to the text-file containing a new-line separated list of students in the class. Spaces in student names will be substituted with an underscore, and no other text processing will be done on student names.

And command-line arguments:
    * `<assignment>` This is the name of the sub-directory in the grading path directory containing this assignment's template. The program can only be run on one assignment template at a time.
    * `-d` flag, if set  will generate a sub-directory for each student in the assignment directory

From the command line:    
`python3 gen_template.py <assignment> -d` or   
`python3 gen_template.py <assignment>`

