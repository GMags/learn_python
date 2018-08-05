import jenkins
import os

username = input("Please enter your username:")
password = input("Please enter your password:")

#server = jenkins.Jenkins('http://159.65.89.217:8080/', username='admin', password='admin123')
server = jenkins.Jenkins('http://159.65.89.217:8080/', username, password)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

print("Total Jenkins Jobs are:", server.jobs_count())

job_name = server.get_all_jobs(2)


server.build_job('Lab Pipeline')

build_repo = "ssh://git@cmestash.chicago.com"
os.system("git clone build_repo")