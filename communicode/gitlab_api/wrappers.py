from communicode import git


def get_projects():
    return git.getprojects()


def create_project(name):
    return git.createproject(name=name)


def get_branches():
    return git.getbranches(1)


def get_project(project_id):
    return git.getproject(project_id)


def get_commit(project_id, commit):
    return git.getrepositorycommit(project_id, commit)
