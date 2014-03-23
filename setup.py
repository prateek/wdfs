from setuptools import setup, find_packages

config = {
      'url':           'URL to get it at.'
    , 'name':          'wdfs'
    , 'author':        'Prateek Rungta'
    , 'license':       'APACHE'
    , 'scripts':       []
    , 'version':       '0.1'
    , 'keywords':      'HDFS Hadoop wdfs'
    , 'packages':      find_packages()
    , 'package_data':  { '': [ '*.json' ] }
    , 'description':   'A Web-HDFS Client'
    , 'download_url':  'http://github.com/prateek/wdfs'
    , 'author_email':  'prungta2@gmail.com'
    , 'install_requires':  [
        'nose'
      , 'sure' 
      , 'requests' 
      , 'HTTPretty' 
      , 'jsonschema' 
    ]
}

setup(**config)
