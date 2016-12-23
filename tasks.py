from invoke import task, run

@task
def hello(ctx):
    # Test Invoke
    print("hello world")

@task
def deploy(ctx):
    local = "build_production/"
    user = "ssh_username"
    server = "servername"
    port = "22"
    remote = "/home/username/public"

    cmd = "rsync -av {local} -e 'ssh -p {port}' {user}@{server}:{remote}".format(
            local=local, port=port, user=user, server=server, remote=remote)
    ctx.run("jigsaw build production")
    ctx.run(cmd)

# Jigsaw
@task
def dev(ctx):
    ctx.run("jigsaw build")

@task
def prod(ctx):
    ctx.run("jigsaw build production")

# Git Commands

@task
def git_push(ctx):
    ctx.run("git -u push origin")

@task
def git_add_all(ctx):
    ctx.run("git add .")

@task
def git_quick_commit(ctx):
    ctx.run("git add .")
    ctx.run("git commit -m 'Update blog.'")


