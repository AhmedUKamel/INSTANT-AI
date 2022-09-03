# Cron jobs

### What is cron jobs
***Abstract:** Is a `job scheduler` on **Unix-based** operating systems.*
> Also known in *Windows* as **Scheduled Tasks**. Tasks can be added through:
> * Windows Task Scheduler
> * PowerShell
> * schtasks.exe

**In linux tasks can be added through:**

    This command 
    ┌───────────── minute (0 - 59)
    │ ┌───────────── hour (0 - 23)
    │ │ ┌───────────── day of the month (1 - 31)
    │ │ │ ┌───────────── month (1 - 12)
    │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
    │ │ │ │ │
    * * * * * <command to execute>
    Please note that * means all

*Execution file / command written in `Shell script`.* <font size='2'>[read more](https://bit.ly/3Be1nUN)</font>
___
#### Resources
Cron Wikipedia - [link](https://bit.ly/3epRXN2)