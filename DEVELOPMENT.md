# Development

Development happens in the `develop` branch, while the latest stable version is
in the `master` branch.

## Setup

As with Gavel, the easiest way to get started hacking on Courthouse is to use 
[Vagrant][vagrant] and run everything inside a virtual machine.

Please contact `sampoder@calhacks.io` for additional help.

### Vagrant

Make sure you have [Vagrant][vagrant] installed on your machine.

To start the VM:

```bash
vagrant up
```

If you need to power off the VM at any point, run:

```bash
vagrant halt
```

To ssh into the VM:

```bash
vagrant ssh
```

**Note: the rest of the commands in this section are meant to be run _inside
the VM_, not on the host machine.**

The project directory gets synchronized to `/courthouse` inside the VM. Once you're
SSHed into the box, install Courthouse's dependencies. You should only need to do
this once, unless Courthouse's dependencies change:

```bash
cd /courthouse
virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
```

Next, set up Courthouse. You should only need to do this once, unless Courthouse's config
options change or Courthouse's database schema changes:

```bash
cp config.vagrant.yaml config.yaml # set good defaults
python initialize.py
```

Finally, you're ready to run Courthouse:

```bash
DEBUG=true python runserver.py
```

Now, on your local machine, you should be able to navigate to
`http://localhost:5000/` and see Courthouse running! You should be able to go to
`http://localhost:5000/admin` and login with the username "admin" with the
password "admin".

If you'd like to enable sending emails, you'll also need to run a celery worker
with:

```bash
celery -A courthouse:celery worker
```

**While developing, you should keep `vagrant rsync-auto` running on the host
machine so that whenever you change any files, they're automatically synced
over to the VM.** When the app running in the VM detects changed files, it'll
automatically restart (because of the debug flag).

## Tips

* While developing, it's helpful to set the environment variable `DEBUG=true`

* If Courthouse's database schema is changed or if the database gets messed up in
  any way, you can reset everything by running (in the Vagrant VM):

    ```bash
    sudo su postgres -c "dropdb courthouse && createdb courthouse"
    python initialize.py
    ```

* This project uses [EditorConfig][editorconfig].
  [Download][editorconfig-download] a plugin for your editor!

[vagrant]: https://www.vagrantup.com/
[virtualenv]: https://virtualenv.pypa.io/en/stable/
[editorconfig]: http://editorconfig.org/
[editorconfig-download]: http://editorconfig.org/#download
