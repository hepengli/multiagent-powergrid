from setuptools import setup, find_packages

setup(name='multiagent-powergrid',
      version='0.0.1',
      description='Multi-Agent Power Grid Environment',
      url='https://github.com/hepengli/multiagent-powergrid',
      author='Hepeng Li',
      author_email='hepengli@uri.edu',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['gym', 'numpy-stl', 'pandapower']
)
