- [ ] sudo apt install supervisor
- [ ] Simple conf file
```
[program:program_name]
command=/path/to/program
autostart=true
autorestart=true
stderr_logfile=/path/to/error/log/file.err.log
stdout_logfile=/path/to/output/log/file.out.log
```
- [ ] supervisorctl reread
  - [ ] To add conf files to supervisor.
- [ ] supervisor update
  - [ ] To update something
- [ ] supervisorctl
  - [ ] To view the processes handled by supervisor.