# listing-EC2-instances

##about

this project uses boto3 to manage AWS EC2 instance snapshots

##configuring

shotty uses configuration file created by AWS cli
'aws configure --profile shotty'

##running

"pipenv run python ./shotty/shotty.py <command> <subcommand> <--project=PROJECT>"

*command* is instances, volumes, snapshots
*subcommand* depends on command
*PROJECT* is optional
