from setuptools import setup

setup(
    name= 'listing-EC2-instances',
    version= '0.1',
    author= 'Sibadatta',
    author_email= 'sibadatta11@outlook.com',
    description= 'A tool to manage AWS EC2 snapshots',
    license= 'GPLv3+',
    packages= ['shotty'],
    url= 'https://github.com/sibadatta/listing-EC2-instances',
    install_requires= ['click','boto3'],
    entry_points= '''
        [console_scripts]
        shotty=shotty.shotty:cli''',
)
