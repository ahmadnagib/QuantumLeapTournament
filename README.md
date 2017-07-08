# QuantumLeap Tournament

QuantumLeap Tournament (QLT) is a python module that uses the PostgreSQL database to keep track of players and matches in a Swiss game tournament.

This project is part of Udacity's Full Stack Web Developer Nanodegree Program. The unit tests and code templates are provided by udacity.

# Documentation

The information related to how to get started is included in this documentation.

- [Quick Start](#quick-start)
- [What is included](#what-is-included)
- [License](#license)

## Quick start

### Local Deployment Software Prerequisites 

- [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) should be installed.
- It is recommended to use [Git Bash](https://git-for-windows.github.io/) or any similar BASH emulation if you are using Windows OS.
- [Udacity Fullstack Nanodegree Virtual Machine](https://github.com/udacity/fullstack-nanodegree-vm) should be downloaded or cloned.

### Deploy QuantumLeap Tournament Test Locally
1. Download [Udacity Fullstack Nanodegree Virtual Machine](https://github.com/udacity/fullstack-nanodegree-vm).
2. Download the [project's files](https://github.com/ahmadnagib/QuantumLeapTournament) and put them altogether in 'tournament' folder of the VM replacing the already existing files.
3. Using Git Bash, move to the path of vagrant folder in the downloaded vm files.
4. Launch the Vagrant VM using `vagrant up` command (This might take a while in the first time).
5. Run `vagrant ssh` command to access the VM.
6. Move to 'tournament' folder containing the project files using `cd /vagrant/tournament`.
7. Connect to PostgreSQL using `psql` command.
8. Build and access the tournament database using `\i tournament.sql` command
9. Run the QL Tournament ten test cases provided by Udacity using `python tournament_test.py`.
10.  If everything has been set up correctly, you will get a message `Success! All tests pass!` at the end of the printed output from the test cases of step 9.

## What is included

Within the downloaded folder you will find the following files:

```
quantumleaptournament-master/
├── tournament.sql
├── tournament.py
├── tournament_test.py
├── LICENSE
├── README.md
```

## License

QuantumLeap Tournament is Copyright © 2017 Ahmad Nagib. It is free software, and may be redistributed under the terms specified in the [LICENSE](/LICENSE) file.
